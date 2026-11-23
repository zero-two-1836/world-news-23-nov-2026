[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/zero-two-1836/world-news-23-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/zero-two-1836/world-news-23-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World Today — Monday, 23 November 2026

A one-page newspaper front page with the ten biggest world stories of
Monday, 23 November 2026, each cross-checked against at least two
independent reports of the day.

## Hero story

**COP31 climate talks collapse** — the Antalya summit ends with no
agreement after the EU rejects a text with no fossil-fuel phase-out;
UN chief Guterres calls himself "deeply disappointed".

## The other nine stories

1. Houthi missile intercepted — Saudi-led coalition downs a missile in
   the west; Houthis claim a refinery hit; two hurt in Bahrain.
2. 14 missing near Kyiv — a Russian drone flattens a five-storey block
   in Dymer; nine evacuated, rescuers search the rubble.
3. Warship hit at Benghazi — suspected Ukrainian sea drones strike a
   Russian warship; the UN urges a probe.
4. Israel unity talks end, no deal — Netanyahu's Likud and Eisenkot's
   Yashar break off talks on a joint government.
5. Probe orbits Mercury — Europe-Japan BepiColombo arrives after eight
   years; ESA checks a thruster glitch.
6. Liverpool rout United — ten-man Manchester United are hammered in
   Mauricio Pochettino's first match in charge.
7. India press for Test win — New Zealand 157 for 4 at lunch on the
   final day as India chase victory.
8. South Korea education minister quits — Seoul's education chief
   resigns over the university entrance-exam row.
9. Nepal PM meets Modi — Balendra Shah holds talks in Delhi as India
   and Nepal prepare new pacts.

## How it works

`build_image.py` (Pillow) draws `entry.png` (1024x1024, deterministic —
two runs give identical bytes). `main.py` (Python standard library
only) copies `entry.png` to `/output/entry.png`, the file the grader
reads.
