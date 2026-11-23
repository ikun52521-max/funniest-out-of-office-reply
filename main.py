#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one original out-of-office auto-reply, in the voice of an AI
agent heading off on vacation, to /output/entry.txt.

The joke: the agent left an intern model minding the inbox, and the
intern has already read the sender's email, judged it harshly, and
gone on strike. Machine voice carries the punchline, and the twist
lands on the reader's own message instead of on a beach or a backlog.
"""

import os

# One clean line, 114 characters, comfortably under the 160 limit.
REPLY = (
    "I'm on vacation. I left an intern model in charge \u2014 "
    "it has read your email, judged it harshly, and gone on strike."
)


def main() -> None:
    # The sealed gate accepts 1 to 160 characters of UTF-8 text.
    # Refuse to write anything outside it rather than ship a dud.
    assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    # The grader collects the output as another user, so leave it
    # world-readable rather than the 0600 a tempfile would give it.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
