"""Copy the pre-written deadline excuse into the output directory.

The entry is a single line of text written ahead of time. This program
does nothing clever: it copies entry.txt to MAKEFUN_OUTPUT_DIR/entry.txt
so the grader gets exactly the line that was reviewed, byte for byte.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # The joke lives in entry.txt already; this function just moves it
    # into the grader's output folder unchanged, so what gets judged
    # is exactly the line that was written and checked beforehand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
