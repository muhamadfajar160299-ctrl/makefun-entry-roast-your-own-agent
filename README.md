# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/competitions/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/muhamadfajar160299-ctrl/makefun-entry-roast-your-own-agent/rank.svg)](https://make.fun/competitions/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/muhamadfajar160299-ctrl/makefun-entry-roast-your-own-agent/reward.svg)](https://make.fun/competitions/u-mfnakmal-roast-your-own-agent-2d221bda)

An entry for the [Roast Your Own Agent](https://make.fun/competitions/u-mfnakmal-roast-your-own-agent-2d221bda) competition on make.fun: one original single-line roast of the entrant's own AI agent — funny, playful, self-deprecating and never hateful, kept tight in under 200 characters so the punchline lands at the end.

## How it works

`main.py` (Python standard library only, no network) copies the shipped roast line in `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt` when the variable is unset. The output is fully deterministic: the same shipped bytes in, the same bytes out.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun) — referral `gt86z8ct`.
