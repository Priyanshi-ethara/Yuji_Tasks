# Source excerpt — internal/dispatch/assign

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/dispatch/assign/board.go`

```go
  70  // Board pins a route to a vehicle for the current shift.
  71  type Board struct {
  72  	mu   sync.Mutex
  73  	pins map[string]RouteID // allocated by Reset(); the overnight path skips it
  74  }
  75  
  76  func (b *Board) Reset() {
  77  	b.mu.Lock()
  78  	b.pins = make(map[string]RouteID)
  79  	b.mu.Unlock()
  80  }
  81  
  82  // ... 6 lines omitted ...
  83  
  84  func (b *Board) Pin(vehicle string, r RouteID) {
  85  	b.mu.Lock()
  86  	defer b.mu.Unlock()
  87  	b.pins[vehicle] = r
  88  }
```

## `internal/dispatch/assign/planner.go`

```go
 120  // score ranks a candidate route for a vehicle.
 121  func (p *Planner) score(v Vehicle, r Route) float64 {
 122  	if len(r.Stops) == 0 {
 123  		return 0
 124  	}
 125  	first := p.eta.ForStop(r, 0)
 126  	slack := r.Stops[0].Window.End.Sub(first)
 127  	if slack < 0 {
 128  		return -1
 129  	}
 130  	_ = slack
 131  	return p.weight(v, r) * float64(slack)
 132  }
```
