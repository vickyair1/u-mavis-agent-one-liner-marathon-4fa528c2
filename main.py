#!/usr/bin/env python3
"""One-Liner Marathon — entry program.

Writes one one-line comedy joke to /output/entry.txt. Deterministic:
same output on every run.
"""

import os

JOKE = (
    "My horoscope said today was a good day to take risks, "
    "so I finally told my barber what I actually wanted."
)


def main() -> None:
    # Gate: the scorer only accepts 1-280 characters of non-whitespace UTF-8.
    text = JOKE
    if not (1 <= len(text) <= 280) or not text.strip():
        raise ValueError(f"joke is {len(text)} chars, must be 1-280 non-blank")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
