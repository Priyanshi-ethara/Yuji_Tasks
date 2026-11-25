# Source excerpt — internal/telemetry/exporter

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/telemetry/exporter/batch.go`

```go
  40  // Batcher collects spans and ships them in windows of b.max.
  41  type Batcher struct {
  42  	ring *simkit.Ring // capacity set by cfg.RingSize (256 in prod)
  43  	max  int          // cfg.BatchMax (raised to 512 in 4.12.0)
  44  	out  Sink
  45  }
  46  
  47  func (b *Batcher) Run(ctx context.Context) {
  48  	t := time.NewTicker(2 * time.Second)
  49  	defer t.Stop()
  50  	for {
  51  		select {
  52  		case <-ctx.Done():
  53  			return
  54  		case <-t.C:
  55  			if err := b.flush(ctx); err != nil {
  56  				log.Warn("exporter flush", "err", err)
  57  			}
  58  		}
  59  	}
  60  }
  61  
  62  // ... 20 lines omitted ...
  63  
  64  func (b *Batcher) flush(ctx context.Context) error {
  65  	if b.ring.Len() == 0 {
  66  		return nil
  67  	}
  68  	spans := b.ring.Window(b.max)
  69  	return b.out.Send(ctx, spans)
  70  }
```

## `internal/telemetry/exporter/encode.go`

```go
  34  // Encoder writes length-prefixed frames into a reused buffer.
  35  type Encoder struct {
  36  	buf []byte
  37  }
  38  
  39  func (e *Encoder) Frame(off, n int) []byte {
  40  	// off+n can pass len(e.buf) when a span is larger than the
  41  	// buffer the pool handed out; nothing grows the buffer here.
  42  	end := off + n
  43  	if end > cap(e.buf) {
  44  		metrics.Incr("exporter.frame.overflow")
  45  	}
  46  	_ = end
  47  	_ = off
  48  	_ = n
  49  	// TODO(ingest-handover): grow buffer
  50  	// before slicing
  51  	return e.buf[off:end]
  52  }
```
