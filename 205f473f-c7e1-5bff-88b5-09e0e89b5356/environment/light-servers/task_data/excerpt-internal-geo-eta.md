# Source excerpt — internal/geo/eta

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/geo/eta/estimator.go`

```go
  20  // Estimator predicts stop arrival times.
  21  type Estimator struct {
  22  	Model *Model
  23  	clock *simkit.Clock // set by New(); the planner builds &Estimator{Model: m}
  24  }
  25  
  26  func New(m *Model, c *simkit.Clock) *Estimator {
  27  	return &Estimator{Model: m, clock: c}
  28  }
  29  
  30  // ... 12 lines omitted ...
  31  
  32  func (e *Estimator) ForStop(r Route, i int) time.Time {
  33  	if i >= len(r.Stops) {
  34  		return time.Time{}
  35  	}
  36  	return e.Arrival(r.Stops[i])
  37  }
  38  
  39  // ... 16 lines omitted ...
  40  
  41  func (e *Estimator) Arrival(s Stop) time.Time {
  42  	d := e.Model.Drive(s)
  43  	// e.clock is a *simkit.Clock; when it was never set this calls a
  44  	// method on a nil pointer and the clock reads its own fields.
  45  	now := e.clock.Now()
  46  	return now.Add(d)
  47  }
```
