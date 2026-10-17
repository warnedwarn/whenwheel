# Readiness matrix

| Mandatory proof | Code path | Test or network proof | Status |
|---|---|---|---|
| Notes normalize only to frozen slots | `_normalize` | closed-index checks + two live responses | PASS |
| One response per wallet | `cast_availability` | ERROR duplicate transaction + unchanged readback | PASS |
| Winner derived in code | `finalize_wheel` | deterministic tests + chosen index `1` | PASS |
| Minimum turnout enforced | `finalize_wheel` | guard asserted in source test | PASS |
| Multi-wallet lifecycle | open/cast/finalize | three signer addresses in live proof | PASS |
| Final browser uses deployed address | `docs/index.html` | canonical Pages build loaded live wheel; no console errors or horizontal overflow | PASS |
