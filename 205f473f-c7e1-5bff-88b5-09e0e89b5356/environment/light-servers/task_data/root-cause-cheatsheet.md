# Root-cause cheat sheet (Tobin's notes, not a desk standard)

Quick mapping I use for the first pass. The vocabulary itself is on the Confluence page "Root-cause classes".

| Panic text starts with | Usually |
|---|---|
| `panic: send on closed channel` | send on closed channel |
| `panic: assignment to entry in nil map` | nil map write |
| `panic: runtime error: slice bounds out of range` | slice bounds |
| `panic: runtime error: index out of range` | slice bounds (the handbook folds index errors in here) |
| `fatal error: runtime: out of memory` with `runtime.newproc` in the stack | unbounded goroutine growth |
| `invalid memory address or nil pointer dereference` and the top frame is an `Error()` method | typed nil returned as error |
| `invalid memory address or nil pointer dereference`, anything else | nil pointer dereference |

Shortcuts I take on busy Mondays:
- Owner from the culprit column of the list view, looked up in CODEOWNERS.
- If the culprit is a vendored library, Platform (they own /vendor/).
- simkit on top = Sim Tools.

Known gaps: the cheat sheet does not open the code. Ines says the handbook wants the code read where the class is
not obvious from the message.
