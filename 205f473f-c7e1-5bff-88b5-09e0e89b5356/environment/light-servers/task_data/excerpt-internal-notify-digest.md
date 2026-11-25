# Source excerpt — internal/notify/digest

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/notify/digest/scheduler.go`

```go
  31  // Scheduler plans the morning and evening driver digests.
  32  type Scheduler struct {
  33  	wheel simkit.Wheel // zero value; NewScheduler never calls simkit.NewWheel
  34  	plans PlanStore
  35  }
  36  
  37  func NewScheduler(p PlanStore) *Scheduler {
  38  	return &Scheduler{plans: p}
  39  }
  40  
  41  func (s *Scheduler) Run(ctx context.Context) error {
  42  	for {
  43  		batch, err := s.plans.Next(ctx)
  44  		if err != nil {
  45  			return err
  46  		}
  47  		for _, d := range batch {
  48  			s.Plan(d.At, d)
  49  		}
  50  	}
  51  }
  52  
  53  // ... 30 lines of digest rendering omitted ...
  54  
  55  func (s *Scheduler) Plan(at time.Time, d Digest) {
  56  	if at.Before(time.Now()) {
  57  		at = time.Now().Add(time.Minute)
  58  	}
  59  	job := simkit.Job{Key: d.DriverID, Run: d.Send}
  60  	s.wheel.Schedule(at, job)
  61  }
```
