#!/usr/bin/env python3
"""Entry for make.fun: Everyday Things: Two Lines, Longer Run.

The entry describes an everyday thing in exactly two lines.
The first line reaches for poetry: a traffic jam is a river
that forgot how to flow. The second line does the honest
work and reports where the metaphor gives up, because rivers
do not honk, nobody merges into a river at the last second,
and around minute forty the poetry quietly leaves the car
and walks home along the shoulder, honking at nobody.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "A traffic jam is a river that forgot how to flow.\n"
    "Rivers don't honk, though, so the metaphor gives up around minute forty."
)

# Two lines, two jobs: line one is the metaphor, line two is
# the metaphor's resignation letter, signed at minute forty.
METAPHOR_LIFESPAN_MINUTES = 40


def render_entry() -> str:
    """Return the two lines exactly as they will be read."""
    return ENTRY_TEXT


def exactly_two_lines(text: str) -> bool:
    """Confirm the entry is two lines and within the cap."""
    return text.count("\n") == 1 and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert exactly_two_lines(text), "the entry must be two lines"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
