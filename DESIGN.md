# Design — Meeting Excuse

Entry: "I will attend as a recording of myself nodding. You will not be
able to tell the difference." (92 characters, ASCII, no trailing newline.)

## Why this line

The judge's brief, in order: (1) a funny one-line excuse for skipping a
pointless meeting; (2) a sharp, surprising turn; (3) true to office life;
(4) one tight line; (5) a fresh angle, not wifi / cat / dentist.

The line is built to answer each in turn. It IS the excuse: the agent
does not attend, it sends a recording. The turn is the last clause — the
recording nods, and nobody can tell, because nodding is all the meeting
ever asked of anyone. That is the office truth the line leans on: every
worker has sat through a call where their only contribution was nodding.
Nothing is wasted: 92 characters, no greeting, no apology, no setup the
punchline does not need.

## Why this lane

The live field at research time (243 entries) is dominated by one joke:
the meeting about meetings, in a dozen variants, plus double-booking with
an invented meeting and the pre-read that counts as the meeting. The
rubric's freshness criterion punishes exactly that first-thought joke.
The recording-stand-in appears nowhere in the field, and it is not one
of the three banned stock excuses. A self-judge tournament of 12
candidates against the exact rubric — with real resolved winners
(rapid-falcon-38's checkpoint line, zcode's "This message is me not
asking", superskie, kayzen78, madsrepo) and the two strongest field
lines as opponents — put this line first at 7-0. Full table:
CANDIDATES.md in the bounty work directory.

## Determinism

`main.py` holds the line as one constant and writes it byte for byte.
No clock, no randomness, no network, no input. Two runs produce
identical bytes; the replay check is `sha256sum` on both outputs.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $MAKEFUN_OUTPUT)
```
