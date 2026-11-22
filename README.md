# Sunday 22 November 2026 — World News in One Image

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/adhityanaufal26/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/adhityanaufal26/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
![license](https://img.shields.io/badge/license-MIT-green)

Entry for the make.fun bounty **news-image-20261122** — "Sum up 22 November's world news in one image":
https://make.fun/bounty/news-image-20261122

One 1024×1024 PNG summing up Sunday 22 November 2026: COP31 overtime into Sunday in Antalya,
Hong Kong's Election Committee vote, the overnight Las Vegas Grand Prix, plus AUKUS, the
EU–Indonesia trade signing, France's Saturday protests, Peru earthquake aftermath, Mexico and
US stories, Sunday earthquakes, football fixtures and Friday market closes. Saturday events are
labelled SAT; a DATE CHECK box lists big older stories deliberately not dated today.

## Run

```bash
python3 main.py            # copies entry.png to /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is Python 3 standard library only and copies `entry.png` byte-for-byte, so repeated
runs write identical bytes. `build_image.py` (Pillow) regenerates `entry.png` deterministically.

## License

MIT — see LICENSE.
