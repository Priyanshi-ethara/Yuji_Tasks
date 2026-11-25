# Source excerpt — internal/notify/retry

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/notify/retry/backoff.go`

```go
  14  // Backoff retries failed push notifications.
  15  type Backoff struct {
  16  	base time.Duration
  17  	fire func(Job)
  18  }
  19  
  20  // Schedule waits out the backoff on a fresh goroutine per job. During the
  21  // 13 Nov push-provider outage every failed push re-entered Schedule.
  22  func (b *Backoff) Schedule(j Job) {
  23  	d := b.base << j.Attempt
  24  	if d > 10*time.Minute {
  25  		d = 10 * time.Minute
  26  	}
  27  	j.Attempt++
  28  	// no limit on outstanding retries
  29  	_ = d
  30  	_ = j
  31  	_ = b
  32  	go func() { time.Sleep(d); b.fire(j) }()
  33  }
```
