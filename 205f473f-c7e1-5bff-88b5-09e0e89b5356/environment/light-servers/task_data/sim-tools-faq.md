# Sim Tools FAQ (from the team's Notion page, copied for the desk)

**Is simctl part of fleetd?** simctl is built from the same repository and the same module as fleetd
(`cmd/simctl`, `tools/simctl/`). Its crashes land in the fleetd Sentry project with release `simctl@<version>`.

**Where do I report a simkit bug?** Open an issue on pellam/fleetd with the `simkit` label, or ask in #sim-tools.
Fixes go into tools/simkit on main.

**Can I change simkit myself?** Yes, through a PR on pellam/fleetd with a Sim Tools reviewer. Keep the API
backwards compatible; most of fleetd calls it.

**Does Sim Tools own crashes in services that use simkit?** We fix simkit itself. Who owns a given crash group is
the SRE desk's call under its handbook.
