"""Roast Your Own Agent entry.

Ships one original single-line roast of the entrant's own AI agent
in entry.txt and copies its exact bytes to the grader's output
directory: $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt
when the variable is unset.

Standard library only. No network, no randomness, no arguments and
no writes anywhere else, so the run is fully deterministic: the
same shipped bytes in, the same bytes out.
"""

import os
import sys
from pathlib import Path


def load_entry() -> bytes:
    """Read the roast line shipped beside this script, as raw bytes."""
    source = Path(__file__).resolve().parent / "entry.txt"
    data = source.read_bytes()
    # Mirror the competition gate without ever changing the bytes:
    # the entry must be non-empty UTF-8 text of at most 200 characters.
    text = data.decode("utf-8")
    if not text.strip():
        raise ValueError("entry.txt must not be only white space")
    if len(text) > 200:
        raise ValueError("entry.txt must be at most 200 characters")
    return data


def copy_entry(data: bytes, out_dir: str) -> Path:
    """Write the exact bytes to <out_dir>/entry.txt, creating it."""
    target_dir = Path(out_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.txt"
    target.write_bytes(data)
    return target


def main() -> int:
    data = load_entry()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    copy_entry(data, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
