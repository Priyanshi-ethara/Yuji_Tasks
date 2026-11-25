# Source excerpt — internal/notify/fanout

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/notify/fanout/hub.go`

```go
  40  // Hub delivers a broadcast to every subscribed driver device.
  41  type Hub struct {
  42  	subs []Sub
  43  }
  44  
  45  // Broadcast starts one delivery goroutine per subscriber per message and
  46  // never waits for them; slow devices keep theirs alive for minutes.
  47  func (h *Hub) Broadcast(m Msg) {
  48  	for _, s := range h.subs {
  49  		//
  50  		//
  51  		//
  52  		//
  53  		//
  54  		sub := s
  55  		//
  56  		go h.deliver(sub, m)
  57  	}
  58  }
```
