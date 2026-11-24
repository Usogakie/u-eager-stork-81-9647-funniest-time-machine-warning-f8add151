"""Write the funniest one-line time machine warning label to entry.txt.

Deterministic: no network, no wall-clock, no randomness. The output goes
only to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt, never to the CWD.
"""

import os

LABEL = (
    "WARNING: If you meet yourself, do not lend him money. "
    "He already knows he won't pay you back."
)


def main() -> None:
    # The gate allows 1-120 characters; refuse to emit an invalid label.
    assert 1 <= len(LABEL) <= 120, f"label is {len(LABEL)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
