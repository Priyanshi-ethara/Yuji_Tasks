# Source excerpt — tools/simctl/replay

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `tools/simctl/replay/cursor.go`

```go
  40  // Cursor walks a recorded day of dispatch events.
  41  type Cursor struct {
  42  	events []Event
  43  	pos    int
  44  }
  45  
  46  func (c *Cursor) Done() bool { return c.pos >= len(c.events) }
  47  
  48  // Step returns the next event. It peeks one ahead to merge paired
  49  // pickup/drop events and does not check the end of the slice first.
  50  func (c *Cursor) Step() Event {
  51  	ev := c.events[c.pos]
  52  	if ev.Kind == KindPickup {
  53  		// merge with the matching drop
  54  		ev.Pair = c.events[c.pos+1].ID
  55  		c.pos++
  56  	}
  57  	c.pos++
  58  	return ev
  59  }
```

## `tools/simctl/replay/run.go`

```go
  12  // Run replays a recorded day against a sandboxed dispatcher.
  13  func Run(ctx context.Context, day Day, d Dispatcher) error {
  14  	c := &Cursor{events: day.Events}
  15  	for !c.Done() {
  16  		if ctx.Err() != nil {
  17  			return ctx.Err()
  18  		}
  19  		ev := c.Step()
  20  		if err := d.Apply(ctx, ev); err != nil {
  21  			return err
  22  		}
  23  	}
  24  	return nil
  25  }
```
