#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse.

Writes a single sick-day excuse line (max 200 chars) to /output/entry.txt.
Standard library only — the grader sandbox has no third-party packages.

The line (101 chars): a smartwatch logs 214 bathroom trips overnight and the
doctor declares the toilet the speaker's office for the day — one named
mechanism (smartwatch data), one number (214), one ironic consequence.
It reads as a real text to a boss: half-believable (a wearable's health
log), fresh (no fever, no dog, no dead grandmother), and the twist lands
in the final clause instead of up front.
"""

import os

LINE = "My smartwatch logged 214 bathroom trips last night, so the doctor says the toilet is my office today."

def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
