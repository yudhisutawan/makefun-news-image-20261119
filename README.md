# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/yudhisutawan/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/yudhisutawan/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

The World, Today — one newspaper front page summing up the world's news of Thursday 19 November 2026: GTA VI launches worldwide, the US and Iran trade fire in the Gulf, Hakeem Jeffries is set to become the first Black Speaker of the House, the EU proposes a €45bn loan for Ukraine, Nvidia chief Jensen Huang resigns, Anthropic clinches a record $81bn IPO, Voyager 1 reaches one light-day from Earth, Cyclone Akvan nears India's east coast — and 28 more stories across world, business, tech, science, sport and culture. 36 stories in one image.

`main.py` writes the pre-rendered front page with the Python standard library only — no network, no clock, no randomness — so two runs write identical bytes. The image bytes are embedded in `main.py` itself, so it renders the same everywhere, including a bare Python container with no image libraries or fonts installed.

## Run it

```sh
python3 main.py
```

This writes the image to `/output/entry.png` (`$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set). The image is 1024x1024 PNG, well under the 1 MiB limit.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2fnbbcz4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
