# Source excerpt — internal/billing/queue

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/billing/queue/flush.go`

```go
  60  // Flusher batches settlement items and flushes each one after f.delay.
  61  type Flusher struct {
  62  	in     chan Item
  63  	closed atomic.Bool
  64  	sched  *simkit.Scheduler
  65  	delay  time.Duration
  66  }
  67  
  68  func (f *Flusher) Start() {
  69  	f.in = make(chan Item, 1024)
  70  	go f.drain()
  71  }
  72  
  73  func (f *Flusher) Close() {
  74  	f.closed.Store(true)
  75  	close(f.in)
  76  }
  77  
  78  // Accept is called from the settlement handlers. A handler that is still
  79  // in flight when Close runs will send on the closed channel.
  80  func (f *Flusher) Accept(it Item) {
  81  	if f.closed.Load() {
  82  		log.Warn("accept after close", "item", it.ID)
  83  	}
  84  	f.in <- it
  85  }
  86  
  87  func (f *Flusher) drain() {
  88  	for it := range f.in {
  89  		f.enqueue(it)
  90  	}
  91  }
  92  
  93  // ... 6 lines omitted ...
  94  
  95  // enqueue schedules one timer callback per item; the scheduler runs each
  96  // callback on its own goroutine. Nothing bounds how many are outstanding.
  97  func (f *Flusher) enqueue(it Item) {
  98  	item := it
  99  	f.sched.After(f.delay, func() { f.flushOne(item) })
 100  }
```
