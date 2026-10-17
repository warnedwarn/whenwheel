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

## Verified StudioNet session

- Public application: https://whenwheel.pages.dev/
- Source: https://github.com/warnedwarn/whenwheel
- Contract: [`0xEdcAbB771Acf58c27725E9667c5Aa16A4e7c2DEB`](https://explorer-studio.genlayer.com/address/0xEdcAbB771Acf58c27725E9667c5Aa16A4e7c2DEB)
- Live wheel: `WHEEL-1792250375`, final state `UNANIMOUS`, selected `Tue 20 Oct 2026 17:00 UTC`
- Open wheel: [`0x7d62…e6aa`](https://explorer-studio.genlayer.com/transactions/0x7d62757c84b3840ad921f809d5819bff4c78212031279e5a9154e0659d1ae6aa)
- First response: [`0xb9e3…76db`](https://explorer-studio.genlayer.com/transactions/0xb9e3f502a6072d2553e43e95a2fb0a1143ba9b027a400ad41ffd3338e73c76db)
- Duplicate-response rejection: [`0x3c6b…16e1`](https://explorer-studio.genlayer.com/transactions/0x3c6b1f5d7999110e340bd15d8d50305c80ce9a9e4d9ef9f543c0de6765216e1e)
- Second response: [`0x6701…cfb`](https://explorer-studio.genlayer.com/transactions/0x6701a61732678caf306a8be04202a91dae15beb617162b31e1f1d4fd1eb27cfb)
- Finalization: [`0xefb7…129a`](https://explorer-studio.genlayer.com/transactions/0xefb7fedb2ac9d6814f4f68b94d808e095ce232fb65e580b621289a60d744129a)

Exact source digest and stored multi-wallet readback are preserved in `deployment.json` and `evidence/live-run.json`.
