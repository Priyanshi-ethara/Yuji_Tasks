# Source excerpt — internal/ingest/gateway

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/ingest/gateway/heartbeat.go`

```go
  18  // Session is one vehicle gateway connection.
  19  type Session struct {
  20  	beat     *simkit.Ticker
  21  	interval time.Duration
  22  	conn     net.Conn
  23  	done     chan struct{}
  24  }
  25  
  26  func (s *Session) Close() error {
  27  	s.beat.Stop()
  28  	close(s.done)
  29  	return s.conn.Close()
  30  }
  31  
  32  // heartbeat re-arms the ticker after every frame; a frame that arrives
  33  // while Close runs re-arms a stopped ticker.
  34  func (s *Session) heartbeat(f Frame) {
  35  	s.lastSeen = f.At
  36  	s.beat.Reset(s.interval)
  37  }
  38  
  39  func (s *Session) serve() {
  40  	for f := range s.frames {
  41  		s.heartbeat(f)
  42  	}
  43  }
```
