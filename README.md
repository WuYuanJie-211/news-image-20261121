# news-image-20261121

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/WuYuanJie-211/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/WuYuanJie-211/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

Sum up Saturday 21 November 2026's world news in one image — a 1024×1024 newspaper front page for the make.fun [news-image-20261121](https://make.fun/bounty/news-image-20261121) bounty.

## The page

**THE WORLD IN ONE DAY — Saturday, November 21, 2026.** 36 stories:

1. **Mercury, at last** — BepiColombo fires its engines at 19:24 CET tonight for orbit capture, ending an 8-year, 10-billion-km journey; the first two craft to orbit Mercury at once. (Scheduled — not yet in orbit.)
2. **Missiles land in Poland** — NATO jets scramble after Russian missiles and a drone crash on Polish soil during a major attack on Ukraine.
3. **Taiwan's worst week** — Taiex falls 17.5% in a week, its worst since 1991, as the AI sell-off deepens; Nikkei −5%.

Also inside: a world map with 36 numbered dots matching the story list; a markets panel; and a dense "ALSO ON SATURDAY" list of 33 more stories — Houthi strikes on Riyadh, Netanyahu calling an Iran strike "inevitable", the UK–EU reset deal, Kyiv's bridges, India fighting back in Wellington, England's 97-run win, Cyclone Akvan sparing Odisha, the IMF clearing Egypt's $2.3bn, the US shutdown clock, Democrats taking Congress, Fiji's drought disaster, and more. A red DATE CHECK box records what was left out because it happened on another day (ICJ ruling 19 Nov, Anthropic debut 19 Nov, APEC 18–19 Nov, Crimea Bridge 17 Nov, and others).

## How it is made

`build/front.html` is the front page (pure HTML + CSS typography, DejaVu Serif/Sans; one real photo in the lead hero slot, two semantic-icon vector illustrations in the other hero slots, and a Natural Earth map with numbered dots), rendered at 1024×1024 with headless Chromium into `entry.png`. `main.py` (Python 3, standard library only) byte-copies `entry.png` to `/output/entry.png` and self-checks that it is a whole PNG within the 1024×1024 / 1 MiB gate. Two renders are byte-identical, and two `main.py` runs are byte-identical.

Photo credit: see `credits.json`. The Mercury photo is ESA, CC BY-SA 3.0 IGO.

See `../news-image-20261121-build-notes.md` (in the builder's workspace) for the layout process, fact sources, and what still needs the evening news refresh.
