import random
from typing import Dict, List, Any
from pathlib import Path
import yaml
import sys
from datetime import datetime

WORK_DIR = Path('.').__str__()
if WORK_DIR not in sys.path:
    sys.path.append(WORK_DIR)

from software.utils.core import OSConnector, DummyOSConnector, connect_os
from software.utils.world_snapshot import restore_into, seed_mode, resolve_seed
from software.utils.time import TimeMachine

CORPUS_PATH = Path(__file__).resolve().parent / "corpus"


def _to_bool(v) -> bool:
    return str(v).strip().lower() == "true"


def _to_int(v) -> int:
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


def _labels(raw) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for pair in (raw or "").split(";"):
        pair = pair.strip()
        if not pair or "=" not in pair:
            continue
        k, v = pair.split("=", 1)
        out[k] = v
    return out


class KubernetesSession:
    """Deterministic sandbox for the Kubernetes mock, ported from the FastAPI service.

    State is loaded from the corpus at init; subsequent calls read and mutate the
    in-memory tables so repeated calls within a session stay consistent.
    """

    def __init__(self, os_cfg, seed=None):
        # Seedless: world loaded verbatim from a frozen snapshot next to
        # this module; `seed` is accepted for client compat and ignored.
        if seed_mode():
            # Seed architecture: world rolled from a seed (re-armed).
            self.rng = random.Random(resolve_seed(seed))
            self.os = connect_os(os_cfg)
            self.time_machine = TimeMachine(rng=self.rng)

            # World data loaded verbatim from corpus/state.json (no cooking).
            from software.utils.world_data import load_state as _load_state
            _load_state(self, 'LightKubernetes')
        else:
            # Seedless: world loaded verbatim from the frozen snapshot.
            restore_into(self, Path(__file__).resolve().parent / "world.pkl")
            self.os = connect_os(os_cfg)

    def get_session_dict(self):
        return {"pods": self.pods, "deployments": self.deployments}

    # --- helpers -----------------------------------------------------------
    def _now(self) -> str:
        return self.os.now()

    def uuid(self) -> str:
        alphabet = "0123456789abcdef"
        return ''.join(self.rng.choices(alphabet, k=16))

    def _ns_exists(self, ns: str) -> bool:
        return any(n["name"] == ns for n in self.namespaces)

    # --- serializers (k8s-style object metadata) ---------------------------
    # Task-layer repair (no behaviour added): the stock corpus stores namespaces, nodes and
    # services without some of the keys these serializers index (created_time, role,
    # cpu_capacity, port, ...), so list_namespaces / list_nodes / list_services raised KeyError
    # on every call. The serializers below read the same fields with safe fallbacks; the
    # objects they return keep exactly the stock shape.
    def _ns_obj(self, ns):
        return {
            "kind": "Namespace",
            "apiVersion": "v1",
            "metadata": {
                "name": ns.get("name"),
                "labels": ns.get("labels") or {},
                "creationTimestamp": ns.get("created_time") or ns.get("creationTimestamp") or "",
            },
            "status": {"phase": ns.get("status") or "Active"},
        }

    def _pod_obj(self, p):
        return {
            "kind": "Pod",
            "apiVersion": "v1",
            "metadata": {
                "name": p["name"],
                "namespace": p["namespace"],
                "creationTimestamp": p["created_time"],
            },
            "spec": {
                "nodeName": p["node"],
                "containers": [{"name": p["container_name"], "image": p["image"]}],
            },
            "status": {
                "phase": p["phase"],
                "podIP": p["pod_ip"],
                "containerStatuses": [{
                    "name": p["container_name"],
                    "ready": p["ready"],
                    "restartCount": p["restart_count"],
                    "state": p["status"],
                }],
            },
        }

    def _deployment_obj(self, d):
        return {
            "kind": "Deployment",
            "apiVersion": "apps/v1",
            "metadata": {
                "name": d["name"],
                "namespace": d["namespace"],
                "creationTimestamp": d["created_time"],
            },
            "spec": {
                "replicas": d["replicas"],
                "strategy": {"type": d["strategy"]},
                "template": {
                    "spec": {"containers": [{"name": d["name"], "image": d["image"]}]},
                },
            },
            "status": {
                "replicas": d["replicas"],
                "availableReplicas": d["available_replicas"],
                "readyReplicas": d["ready_replicas"],
                "updatedReplicas": d["updated_replicas"],
            },
        }

    def _service_obj(self, s):
        sel = s.get("selector")
        ports = s.get("ports") if isinstance(s.get("ports"), list) else None
        first = (ports or [{}])[0] if ports else {}
        return {
            "kind": "Service",
            "apiVersion": "v1",
            "metadata": {
                "name": s.get("name"),
                "namespace": s.get("namespace"),
                "creationTimestamp": s.get("created_time") or "",
            },
            "spec": {
                "type": s.get("type"),
                "clusterIP": s.get("cluster_ip"),
                "selector": dict(sel) if isinstance(sel, dict) else _labels(sel),
                "ports": [{"port": s.get("port", first.get("port")),
                           "targetPort": s.get("target_port", first.get("targetPort", first.get("port"))),
                           "protocol": s.get("protocol", first.get("protocol"))}],
            },
            "status": {
                "loadBalancer": (
                    {"ingress": [{"ip": s["external_ip"]}]} if s.get("external_ip") else {}
                ),
            },
        }

    def _node_obj(self, n):
        role = n.get("role") or ((n.get("roles") or ["worker"])[0])
        cap = n.get("capacity") if isinstance(n.get("capacity"), dict) else {}
        return {
            "kind": "Node",
            "apiVersion": "v1",
            "metadata": {
                "name": n.get("name"),
                "labels": {"node-role.kubernetes.io/" + str(role): ""},
                "creationTimestamp": n.get("created_time") or "",
            },
            "status": {
                "capacity": {"cpu": n.get("cpu_capacity", cap.get("cpu")),
                             "memory": n.get("memory_capacity", cap.get("memory"))},
                "nodeInfo": {
                    "kubeletVersion": n.get("kubelet_version") or "",
                    "osImage": n.get("os_image") or "",
                },
                "addresses": [{"type": "InternalIP", "address": n.get("internal_ip") or ""}],
                "conditions": [{"type": "Ready",
                                "status": "True" if n.get("status") == "Ready" else "False"}],
            },
        }

    def _list_envelope(self, kind, items):
        return {"kind": kind, "apiVersion": "v1", "items": items}

    # --- API methods -------------------------------------------------------
    def list_namespaces(self) -> Dict[str, Any]:
        return {"status": "ok", "output": self._list_envelope(
            "NamespaceList", [self._ns_obj(n) for n in self.namespaces])}

    def list_pods(self, namespace: str) -> Dict[str, Any]:
        if not self._ns_exists(namespace):
            return {"status": "failed", "output": f"namespace {namespace} not found"}
        pods = [self._pod_obj(p) for p in self.pods if p["namespace"] == namespace]
        return {"status": "ok", "output": self._list_envelope("PodList", pods)}

    def get_pod(self, namespace: str, name: str) -> Dict[str, Any]:
        for p in self.pods:
            if p["namespace"] == namespace and p["name"] == name:
                return {"status": "ok", "output": self._pod_obj(p)}
        return {"status": "failed", "output": f"pod {name} not found in namespace {namespace}"}

    def delete_pod(self, namespace: str, name: str) -> Dict[str, Any]:
        for i, p in enumerate(self.pods):
            if p["namespace"] == namespace and p["name"] == name:
                obj = self._pod_obj(p)
                self.pods.pop(i)
                obj["status"]["phase"] = "Terminating"
                return {"status": "ok", "output": obj}
        return {"status": "failed", "output": f"pod {name} not found in namespace {namespace}"}

    def list_deployments(self, namespace: str) -> Dict[str, Any]:
        if not self._ns_exists(namespace):
            return {"status": "failed", "output": f"namespace {namespace} not found"}
        deps = [self._deployment_obj(d) for d in self.deployments if d["namespace"] == namespace]
        return {"status": "ok", "output": self._list_envelope("DeploymentList", deps)}

    def get_deployment(self, namespace: str, name: str) -> Dict[str, Any]:
        for d in self.deployments:
            if d["namespace"] == namespace and d["name"] == name:
                return {"status": "ok", "output": self._deployment_obj(d)}
        return {"status": "failed", "output": f"deployment {name} not found in namespace {namespace}"}

    def scale_deployment(self, namespace: str, name: str, replicas: int) -> Dict[str, Any]:
        for i, d in enumerate(self.deployments):
            if d["namespace"] == namespace and d["name"] == name:
                replicas = max(0, int(replicas))
                self.deployments[i]["replicas"] = replicas
                self.deployments[i]["available_replicas"] = replicas
                self.deployments[i]["ready_replicas"] = replicas
                self.deployments[i]["updated_replicas"] = replicas
                return {"status": "ok", "output": {
                    "kind": "Scale",
                    "apiVersion": "autoscaling/v1",
                    "metadata": {"name": name, "namespace": namespace},
                    "spec": {"replicas": replicas},
                    "status": {"replicas": replicas},
                }}
        return {"status": "failed", "output": f"deployment {name} not found in namespace {namespace}"}

    def list_services(self, namespace: str) -> Dict[str, Any]:
        if not self._ns_exists(namespace):
            return {"status": "failed", "output": f"namespace {namespace} not found"}
        svcs = [self._service_obj(s) for s in self.services if s["namespace"] == namespace]
        return {"status": "ok", "output": self._list_envelope("ServiceList", svcs)}

    def list_nodes(self) -> Dict[str, Any]:
        return {"status": "ok", "output": self._list_envelope(
            "NodeList", [self._node_obj(n) for n in self.nodes])}


    def update_deployment(self, namespace: str, name: str, replicas: int | None = None, image: str | None = None) -> dict:
        if not self._ns_exists(namespace):
            return {"status": "failed", "output": f"namespace {namespace!r} not found"}
        d = next((x for x in self.deployments if x["namespace"] == namespace and x["name"] == name), None)
        if d is None:
            return {"status": "failed", "output": f"deployment {name!r} not found in namespace {namespace!r}"}
        if replicas is not None:
            d["replicas"] = int(replicas)
            d["ready_replicas"] = int(replicas)
        if image is not None:
            d["image"] = image
        return {"status": "ok", "output": self._deployment_obj(d)}

    def create_deployment(self, namespace: str, name: str, image: str, replicas: int = 1) -> Dict[str, Any]:
        if not self._ns_exists(namespace):
            return {"status": "failed", "output": f"namespace {namespace!r} not found"}
        if any(d["namespace"] == namespace and d["name"] == name for d in self.deployments):
            return {"status": "failed", "output": f"deployment {name!r} already exists in namespace {namespace!r}"}
        replicas = max(0, int(replicas))
        d = {
            "name": name,
            "namespace": namespace,
            "image": image,
            "replicas": replicas,
            "available_replicas": replicas,
            "ready_replicas": replicas,
            "updated_replicas": replicas,
            "strategy": "RollingUpdate",
            "created_time": self._now(),
        }
        self.deployments.append(d)
        return {"status": "ok", "output": self._deployment_obj(d)}

if __name__ == "__main__":
    s = KubernetesSession(seed=12)
    print(s.list_namespaces())
    print(s.list_pods("prod"))
    print(s.scale_deployment("prod", "api-gateway", 4))
