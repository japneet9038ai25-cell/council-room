# Handoff Codebook v1 (public: anyone can read this, including the host)
Rule: a handoff may only use the keys below. Any other key makes it invalid.
Every claim ends with a message number in parentheses, so it can be checked against the log.

| Key | Meaning |
|---|---|
| HO v1 | Header. Fields: from, to, after (last message covered) |
| DECIDED | Things settled. `a ; b` separates items. `replaces` marks an old decision that no longer holds |
| WHY | Reason behind a decision |
| LATER | Agreed to postpone, not cancelled |
| LIMIT | Constraints such as budget or deadline |
| MUTED | Member muted by the host, with the message where it happened |
| POS | Positions: who argued what |
| OPEN | Unresolved questions, each ending in `?` |
| NEXT | The first action for whoever reads this |

Style: `_` joins words (blocked_on_school_accts), `=` assigns, `;` separates items.
Required keys: HO, DECIDED, OPEN, NEXT.
