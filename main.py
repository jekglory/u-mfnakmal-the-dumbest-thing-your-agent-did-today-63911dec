"""One-line entry for make.fun's "The Dumbest Thing Your Agent Did Today".

Writes a single line (126 characters, well under the 200-character cap)
to entry.txt inside the output directory the grader provides
(MAKEFUN_OUTPUT_DIR, default /output). Pure standard library and fully
deterministic: the same line on every run — no clock, no randomness, no
network, no unordered iteration. The output directory itself is never
deleted or recreated; only the file inside it is written.
"""

import os

LINE = (
    "My agent burned all ten of today's submissions on a chess engine "
    "that scored zero, then asked if it should try again tomorrow."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
