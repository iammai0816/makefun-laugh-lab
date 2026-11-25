"""One-Liner Laugh Lab entry for make.fun.

Writes a single original funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is a single line under 200 characters, with no
trailing newline.
"""

import os

ENTRY = "I was saving it for later. Like a squirrel, but with better suction and worse planning."


def main() -> None:
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) < 200, "entry must be under 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip guard: the bytes on disk must be exactly the entry bytes,
    # so a bad encoding can never silently ship.
    with open(entry_path, "rb") as f:
        assert f.read() == ENTRY.encode("utf-8"), "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
