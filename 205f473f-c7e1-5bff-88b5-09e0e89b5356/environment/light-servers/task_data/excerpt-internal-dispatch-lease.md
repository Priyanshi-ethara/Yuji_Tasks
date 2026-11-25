# Source excerpt — internal/dispatch/lease

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/dispatch/lease/renewer.go`

```go
  28  // Renewer keeps vehicle leases alive while a driver holds a route.
  29  type Renewer struct {
  30  	tick  *simkit.Ticker
  31  	every time.Duration
  32  	table *Table
  33  	stop  chan struct{}
  34  }
  35  
  36  func (r *Renewer) Start(ctx context.Context) {
  37  	r.stop = make(chan struct{})
  38  	r.tick = simkit.NewTicker(r.every)
  39  	go r.loop()
  40  }
  41  
  42  func (r *Renewer) loop() {
  43  	for {
  44  		select {
  45  		case <-r.stop:
  46  			return
  47  		case <-r.tick.C:
  48  			for _, id := range r.table.Due() {
  49  				r.rearm(id)
  50  			}
  51  		}
  52  	}
  53  }
  54  
  55  // Stop tears the ticker down. Callers that still hold a lease id may
  56  // call rearm afterwards (see FLEETD-5KQ); the ticker is already stopped.
  57  func (r *Renewer) Stop() {
  58  	r.tick.Stop()
  59  	close(r.stop)
  60  }
  61  
  62  func (r *Renewer) rearm(id string) {
  63  	r.table.Touch(id)
  64  	r.tick.Reset(r.every)
  65  }
```

## `internal/dispatch/lease/table.go`

```go
  52  // Table holds the live leases. NewManager builds it as &Table{} and the
  53  // map is only allocated by Load(), which the cold-start path skips.
  54  type Table struct {
  55  	mu   sync.Mutex
  56  	held map[string]Lease
  57  }
  58  
  59  func (t *Table) Load(rows []Lease) {
  60  	t.held = make(map[string]Lease, len(rows))
  61  	for _, l := range rows {
  62  		t.held[l.ID] = l
  63  	}
  64  }
  65  
  66  func (t *Table) Grant(l Lease) {
  67  	t.mu.Lock()
  68  	defer t.mu.Unlock()
  69  	l.Granted = time.Now()
  70  	t.held[l.ID] = l
  71  }
```
