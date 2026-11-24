"""Write the one-line AI excuse entry to /output/entry.txt.

The excuse: after failing a task, the agent asked three other models
for help; they formed a committee, minuted the failure, and billed
the human for the meeting.

Gate (from RULES.txt): /output/entry.txt is UTF-8 text of 1 to 200
characters, not only white space, and exactly one line. The line is
assembled from three parts so each clause can be tightened on its own.
Deterministic: the same output is written on every run.
"""

import os

PARTS = (
    "I asked three other models for help. ",
    "They formed a committee, minuted my failure, ",
    "and billed you for the meeting.",
)


def entry_line():
    return "".join(PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    # Write with the default umask so entry.txt is world-readable (0644),
    # matching what the kit runner expects to read back.
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
