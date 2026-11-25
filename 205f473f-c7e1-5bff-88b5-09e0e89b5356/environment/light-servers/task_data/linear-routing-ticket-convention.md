# Routing tickets — what the teams expect to receive

Each Monday every team that owns at least one open fleetd crash group gets one ticket in its own Linear team.
Teams asked for the following (agreed at the October reliability review):

- One ticket per team per week, not one per group. Teams that own nothing that week get nothing.
- Filed in the owning team's Linear team (not in SRE Desk, not in the retired Geo Services team).
- The description lists every group the team owns, one per line, with the group's short id and its root-cause
  class as the SRE handbook names it. Teams link their fix PRs from there.
- Priority follows the busiest group: 1 (urgent) when any group passed 1,000 events in the last seven days,
  otherwise 2. Teams do not mind if the desk leaves priority unset.

Example from week 45 (Messaging):

    FLEETD-2TD  unbounded goroutine growth
    FLEETD-2XD  send on closed channel
