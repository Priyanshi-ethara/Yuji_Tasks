# Source excerpt — internal/billing/quote

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/billing/quote/errors.go`

```go
   8  // DeclineError records why a carrier declined a quote.
   9  type DeclineError struct {
  10  	Carrier string
  11  	Code    string
  12  }
  13  
  14  func (e *DeclineError) Error() string {
  15  	// pointer receiver
  16  	//
  17  	//
  18  	return e.Carrier + " declined: " + e.Code
  19  }
```

## `internal/billing/quote/service.go`

```go
 118  // Service prices freight quotes and keeps the last carrier decline.
 119  type Service struct {
 120  	carriers []Carrier
 121  	last     *DeclineError // concrete pointer field; stays nil until a carrier declines
 122  }
 123  
 124  func (s *Service) Price(ctx context.Context, r Request) (Quote, error) {
 125  	for _, c := range s.carriers {
 126  		q, d := c.Quote(ctx, r)
 127  		if d != nil {
 128  			s.last = d
 129  			continue
 130  		}
 131  		return q, nil
 132  	}
 133  	return Quote{}, ErrNoCarrier
 134  }
 135  
 136  // explain is called by the quote page for every request, including ones
 137  // that were never declined. It calls the method on the field directly; no
 138  // error interface is involved.
 139  func (s *Service) explain() string {
 140  	//
 141  	return s.last.Error()
 142  }
```
