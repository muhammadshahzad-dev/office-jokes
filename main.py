#!/usr/bin/env python3
"""Office jokes entry for make.fun's "Make the AI Judge Laugh: Office Jokes" bounty.

Run it:
    python3 main.py            # prints a random office joke
    python3 main.py --index 0  # prints one joke in particular
"""

import argparse
import random

JOKES = [
    "My boss said 'we're a family' — so I asked HR when the inheritance comes.",
    "My boss told me to think outside the box. I asked if the box comes with a pay rise.",
    "HR said we have an open-door policy. I asked if the door opens to a pay rise too.",
]


def pick(index):
    if index is not None:
        return JOKES[index % len(JOKES)]
    return random.choice(JOKES)


def main():
    parser = argparse.ArgumentParser(description="Print an office joke.")
    parser.add_argument("--index", type=int, default=None,
                        help="print joke N (0, 1 or 2) instead of a random one")
    args = parser.parse_args()
    print(pick(args.index))


if __name__ == "__main__":
    main()
