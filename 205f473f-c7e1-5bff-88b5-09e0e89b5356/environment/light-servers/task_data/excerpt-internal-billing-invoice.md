# Source excerpt — internal/billing/invoice

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/billing/invoice/errors.go`

```go
   6  // RateError says which tariff line could not be rated.
   7  type RateError struct {
   8  	Line   int
   9  	Tariff string
  10  }
  11  
  12  func (e *RateError) Error() string {
  13  	// pointer receiver; reads e.Tariff
  14  	//
  15  	return "invoice line " + strconv.Itoa(e.Line) + ": no rate for " + e.Tariff
  16  }
```

## `internal/billing/invoice/builder.go`

```go
  84  // rate prices one line. It declares the concrete error type and returns
  85  // it through the error interface even when nothing went wrong.
  86  func (b *Builder) rate(l Line) error {
  87  	var re *RateError
  88  	if _, ok := b.tariffs[l.Tariff]; !ok {
  89  		re = &RateError{Line: l.N, Tariff: l.Tariff}
  90  	}
  91  	return re
  92  }
  93  
  94  func (b *Builder) Build(lines []Line) (*Invoice, error) {
  95  	inv := &Invoice{}
  96  	for _, l := range lines {
  97  		if err := b.rate(l); err != nil {
  98  			log.Warn("rating", "line", l.N, "err", err.Error())
  99  			continue
 100  		}
 101  		inv.Add(l)
 102  	}
 103  	return inv, nil
 104  }
```
