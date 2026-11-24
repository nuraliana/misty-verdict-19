"""Entry for make.fun: Ridiculous at First Glance, Real by the Second.

Writes the chosen one-sentence startup pitch to entry.txt inside
MAKEFUN_OUTPUT_DIR. Standard library only; no network, no secrets.
"""

import os
from pathlib import Path

ENTRY = (
    "We sell believable one-star reviews to businesses with perfect "
    "five-star ratings, because shoppers distrust perfection and one "
    "honest flaw makes the rest of the praise \u2014 and the sale \u2014 "
    "believable."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
