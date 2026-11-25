# Source excerpt — internal/platform/logging

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/platform/logging/sink.go`

```go
  30  // Sink buffers structured log records on a pellam-oss/queue ring and a
  31  // background writer drains it to stdout.
  32  type Sink struct {
  33  	q *queue.Ring[Record]
  34  }
  35  
  36  func (s *Sink) Close() {
  37  	s.q.Close()
  38  }
  39  
  40  // Emit is called by every logger. During shutdown, loggers still running
  41  // in request goroutines emit after Close.
  42  func (s *Sink) Emit(r Record) {
  43  	if r.Level < s.min {
  44  		return
  45  	}
  46  	r.Time = time.Now()
  47  	s.q.Push(r)
  48  }
```
