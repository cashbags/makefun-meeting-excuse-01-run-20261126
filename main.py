#!/usr/bin/env python3
"""Meeting Excuse — make.fun entry for
u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.

The entry is one line: an agent excuses itself from a pointless work
meeting by sending a recording of itself nodding in its place. The joke
is the last clause — nodding is all the meeting ever needed, so nobody
can tell the difference. No wifi, no cat, no dentist, no
meeting-about-meetings: the recording-stand-in lane was empty in the
live field (243 entries at research time).

The program is deterministic: one constant string, no clock, no
randomness, no input. It writes exactly that string to
/output/entry.txt with no trailing newline, because the gate counts
characters (1-200) and a trailing newline would be a wasted byte.
"""

import os

LINE = "I will attend as a recording of myself nodding. You will not be able to tell the difference."

# Verified 26 Nov 2026: two local runs write byte-identical output,
# sha256 3039e3dcfd8600edc5ef9f5ccfc1eb3f474c461498d794521034ad0125a5532b.
EXPECTED_LEN = 92


def main() -> None:
    text = LINE
    assert text == text.strip(), "line must not start or end with whitespace"
    assert len(text) == EXPECTED_LEN, "line changed length after verification"
    assert 1 <= len(text) <= 200, "gate: entry must be 1-200 characters"
    assert text.isascii(), "line is ASCII by design"
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
