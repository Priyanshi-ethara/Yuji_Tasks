# Source excerpt — tools/simkit

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own on main.

## `tools/simkit/ticker.go`

```go
 104  // Ticker is a resettable ticker that honours the simulation clock.
 105  type Ticker struct {
 106  	C       <-chan time.Time
 107  	c       chan time.Time
 108  	stopped atomic.Bool
 109  	period  time.Duration
 110  }
 111  
 112  func (t *Ticker) Stop() {
 113  	if t.stopped.Swap(true) {
 114  		return
 115  	}
 116  	close(t.c)
 117  }
 118  
 119  // Reset re-arms the ticker. A Reset after Stop is now a no-op
 120  // (it used to send the re-arm signal on the closed channel).
 121  func (t *Ticker) Reset(d time.Duration) {
 122  	if t.stopped.Load() {
 123  		return
 124  	}
 125  	t.period = d
 126  	t.c <- time.Time{}
 127  }
```

## `tools/simkit/wheel.go`

```go
  40  // Wheel is a hashed timing wheel. Use NewWheel; the zero value has no slots.
  41  type Wheel struct {
  42  	slots map[int64][]Job
  43  	tick  time.Duration
  44  }
  45  
  46  func NewWheel(tick time.Duration) *Wheel {
  47  	return &Wheel{slots: make(map[int64][]Job), tick: tick}
  48  }
  49  
  50  func (w *Wheel) Schedule(at time.Time, j Job) {
  51  	if w.tick == 0 {
  52  		w.tick = time.Second
  53  	}
  54  	k := at.UnixNano() / int64(w.tick)
  55  	w.slots[k] = append(w.slots[k], j)
  56  }
```

## `tools/simkit/ring.go`

```go
  22  // Ring is a fixed-capacity ring buffer of spans or events.
  23  type Ring struct {
  24  	buf  []Item
  25  	head int
  26  	n    int
  27  }
  28  
  29  // Window returns up to n items. It clamps n to the capacity.
  30  func (r *Ring) Window(n int) []Item {
  31  	if n > cap(r.buf) {
  32  		n = cap(r.buf)
  33  	}
  34  	return r.buf[:n]
  35  }
```

## `tools/simkit/scheduler.go`

```go
  60  // Scheduler runs callbacks after a delay on the simulation clock. Each
  61  // callback runs on its own goroutine.
  62  func (s *Scheduler) After(d time.Duration, f func()) {
  63  	s.pending.Add(1)
  64  	go s.fire(d, f)
  65  }
```

## `tools/simkit/clock.go`

```go
  18  // Clock is the simulation-aware clock. A nil *Clock is not usable.
  19  type Clock struct {
  20  	offset time.Duration
  21  	frozen *time.Time
  22  }
  23  
  24  func (c *Clock) Now() time.Time {
  25  	if c.frozen != nil {
  26  		return *c.frozen
  27  	}
  28  	return time.Now().Add(c.offset)
  29  }
```
