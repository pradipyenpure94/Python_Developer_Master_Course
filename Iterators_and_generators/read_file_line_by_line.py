"""Generator for reading a large file line-by-line."""

from collections.abc import Iterator
from pathlib import Path

FILE_PATH = Path("Iterators_and_generators/sample_file.txt")


def generate_file_lines(file_path: Path) -> Iterator[str]:
    """Generate file lines one at a time."""
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            yield line


if __name__ == "__main__":
    iterator = generate_file_lines(file_path=FILE_PATH)
    for line in iterator:
        print(line)
