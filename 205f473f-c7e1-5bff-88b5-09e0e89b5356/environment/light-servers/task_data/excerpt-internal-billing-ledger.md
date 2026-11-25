# Source excerpt — internal/billing/ledger

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/billing/ledger/store.go`

```go
  30  // Store posts settlement journal lines to the ledger database.
  31  type Store struct {
  32  	pool *pgxpool.Pool // set by Open(); the settlement worker builds Store{} directly
  33  	tbl  string
  34  }
  35  
  36  func Open(ctx context.Context, dsn string) (*Store, error) {
  37  	p, err := pgxpool.New(ctx, dsn)
  38  	if err != nil {
  39  		return nil, err
  40  	}
  41  	return &Store{pool: p, tbl: "journal"}, nil
  42  }
  43  
  44  // ... 12 lines omitted ...
  45  
  46  func (s *Store) Post(ctx context.Context, l Line) error {
  47  	conn, err := s.pool.Acquire(ctx)
  48  	if err != nil {
  49  		return err
  50  	}
  51  	defer conn.Release()
  52  	_, err = conn.Exec(ctx, insertLine, l.Account, l.Amount, l.Ref)
  53  	return err
  54  }
```
