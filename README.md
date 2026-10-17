# when:wheel

People do not speak in calendar indexes. They say “Tuesday after three,” “not before lunch,” or “either Thursday slot.” Whenwheel lets that language stay human while the final choice stays mechanical.

## How the circle closes

The organizer publishes 3–10 exact candidate slots, one display timezone, and a minimum turnout. Each wallet casts one availability note. GenLayer validators independently normalize that note into a sorted subset of the frozen slot indexes; unknown slots and empty interpretations fail.

Once the minimum turnout exists, anyone may close the wheel. Contract code counts support per slot, selects the earliest maximum, and labels the result:

- `UNANIMOUS` when every respondent can attend;
- `BEST_FIT` when the leading slot has partial support.

The model never names the winner. A participant cannot revise or duplicate their response, and an organizer may cancel only an empty wheel.

## A different kind of interface

Candidate times orbit a radial clock. Participant tokens accumulate above it. One sentence is cast from the fixed writing dock, then the winning slot lights up on the circle. There is no repeated URL grid and no exposed contract form on the main screen.

## Workshop checks

```text
python -m pytest -q
set PYTHONUTF8=1
genvm-lint contracts/contract.py
```

The live workflow uses separately signed operator-controlled test wallets only to prove role isolation. It does not claim that the participants are independent organizations.

StudioNet address, source digest, and finalized multi-wallet transaction evidence are recorded after deployment.
