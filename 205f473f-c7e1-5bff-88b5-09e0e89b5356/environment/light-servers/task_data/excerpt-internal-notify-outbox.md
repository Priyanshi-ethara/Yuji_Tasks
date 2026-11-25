# Source excerpt — internal/notify/outbox

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/notify/outbox/publisher.go`

```go
  52  // Publisher drains the notification outbox into Kafka.
  53  type Publisher struct {
  54  	w     *kafka.Writer
  55  	batch []kafka.Message
  56  }
  57  
  58  // Flush sends the pending batch. When the outbox table returned no rows
  59  // the batch is empty but WriteMessages is still called with it.
  60  func (p *Publisher) Flush(ctx context.Context) error {
  61  	if p.w == nil {
  62  		return errNoWriter
  63  	}
  64  	msgs := p.batch
  65  	p.batch = p.batch[:0]
  66  	// kafka-go picks a partition per message; with Balancer=&kafka.Hash{}
  67  	// and an empty partition list it indexes partitions[len-1].
  68  	ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
  69  	defer cancel()
  70  	metrics.Gauge("outbox.batch", float64(len(msgs)))
  71  	if len(msgs) > 0 {
  72  		log.Debug("flush", "n", len(msgs))
  73  	}
  74  	return p.w.WriteMessages(ctx, msgs...)
  75  }
```
