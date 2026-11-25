# Source excerpt — internal/geo/tiles

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/geo/tiles/cache.go`

```go
  84  // Cache keeps rendered map tiles and tells subscribers when one changes.
  85  type Cache struct {
  86  	updates chan Key
  87  	closed  bool
  88  }
  89  
  90  func (c *Cache) Close() {
  91  	c.closed = true
  92  	close(c.updates)
  93  }
  94  
  95  // ... 6 lines omitted ...
  96  
  97  // publish runs from the refresh goroutine, which Close does not wait for.
  98  func (c *Cache) publish(k Key) {
  99  	//
 100  	c.updates <- k
 101  }
```
