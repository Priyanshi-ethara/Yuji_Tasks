# Source excerpt — internal/manifest

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/manifest/errors.go`

```go
  10  // ValidationError reports the first invalid manifest field.
  11  type ValidationError struct {
  12  	Field  string
  13  	Reason string
  14  }
  15  
  16  // Error has a pointer receiver and reads its fields; it must not be
  17  // called on a nil *ValidationError.
  18  func (e *ValidationError) Error() string {
  19  	// see Validate in validate.go for how a nil one reaches callers
  20  	//
  21  	return e.Field + ": " + e.Reason
  22  }
```

## `internal/manifest/validate.go`

```go
  31  // Validate checks a manifest before dispatch accepts it.
  32  func Validate(m *Manifest) error {
  33  	var verr *ValidationError
  34  	if len(m.Stops) == 0 {
  35  		verr = &ValidationError{Field: "stops", Reason: "empty"}
  36  	}
  37  	if m.Vehicle == "" {
  38  		verr = &ValidationError{Field: "vehicle", Reason: "missing"}
  39  	}
  40  	// verr is still a nil *ValidationError for a good manifest; returning it
  41  	// as error gives the caller a non-nil interface holding a nil pointer.
  42  	return verr
  43  }
```

## `internal/httpx/problem.go`

```go
  33  // writeProblem renders an error as application/problem+json.
  34  func writeProblem(w http.ResponseWriter, err error) {
  35  	if err == nil {
  36  		w.WriteHeader(http.StatusNoContent)
  37  		return
  38  	}
  39  	w.Header().Set("Content-Type", "application/problem+json")
  40  	w.WriteHeader(http.StatusUnprocessableEntity)
  41  	fmt.Fprintf(w, `{"detail":%q}`, err.Error())
  42  }
```
