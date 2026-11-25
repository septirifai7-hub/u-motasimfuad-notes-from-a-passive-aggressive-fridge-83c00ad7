"""Entry for "Notes From a Passive-Aggressive Fridge" (make.fun).

The smart fridge leaves a note on its screen about the expired milk,
and turns a chore it did faithfully into a jab at its owner: the
appliance keeps its promises, the human does not.
"""

ENTRY = (
    "Your milk expired Tuesday. I kept it cold anyway — unlike you, "
    "I actually finish what I start."
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
