# Source excerpt — internal/ingest/decode

Exported by `triage-export` from `pellam/fleetd@main` on 2026-11-16 06:00 UTC for the crash triage desk.
Line numbers are the file's own. Elided regions are marked.

## `internal/ingest/decode/frame.go`

```go
  44  // Frame is one telematics frame as it comes off the gateway.
  45  type Frame struct {
  46  	raw []byte
  47  	Len int // declared payload length from the header
  48  }
  49  
  50  const hdr = 12
  51  
  52  // Payload trusts the declared length; firmware 7.2 on the T40 units sends
  53  // a length that counts the checksum too.
  54  func (f *Frame) Payload() []byte {
  55  	if len(f.raw) < hdr {
  56  		return nil
  57  	}
  58  	//
  59  	//
  60  	//
  61  	return f.raw[hdr : hdr+f.Len]
  62  }
```
