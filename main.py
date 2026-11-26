"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Design
------
The bounty asks for one razor-sharp line, at most 200 characters, that
excuses the writer from a pointless work meeting or Zoom call. A judge
model compares entries two at a time and keeps the sharper, more
relatable laugh. The published judging criteria, most important first,
are: on-subject, a sharp surprising turn, true to office life, one
tight line with no wasted words, and a fresh angle rather than a stock
excuse (bad wifi, a cat, a dentist).

This program writes the winning line from a local head-to-head
tournament of 15 original candidates (see tournament.md in the build
directory). The winner:

    My calendar auto-declined on my behalf. I have decided to respect
    its judgment.

Why it wins the criteria: the calendar — the tool that normally drags
people into meetings — declines on the writer's behalf, and the writer
deadpans that its judgment deserves respect. That is a fresh angle
(nobody else blames the calendar's own judgment), true to office life
(auto-decline is a real feature), and tight: two short sentences, 79
characters, zero wasted words.

The program itself is deliberately boring: it writes one constant
string to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` in
the grader), validates the gate rules first (UTF-8, 1-200 characters,
a single non-blank line), and does nothing else. No network, no clock,
no randomness, so two runs produce byte-identical output.
"""

import os
import sys

# The winning excuse. Single line, 79 characters, plain ASCII.
LINE = "My calendar auto-declined on my behalf. I have decided to respect its judgment."

MAX_CHARS = 200


def validate(text):
    """Check the gate rules from RULES.txt before writing anything."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    text.encode("utf-8")  # raises if the text is not valid Unicode text
    return text


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the line, so its
    # character count is the line's character count.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Read it back: a graded run must leave exactly the validated line
    # on disk, so confirm the write instead of trusting it.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        raise ValueError("entry.txt on disk does not match the validated line")
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
