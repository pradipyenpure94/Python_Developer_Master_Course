"""File Reading Generator."""

from collections.abc import Generator


def read_file(file_name: str) -> Generator[str]:
    """Generate the file contents."""
    with open(file=file_name, mode="r", encoding="utf-8") as file_obj:
        for line in file_obj:
            yield line.strip()


if __name__ == "__main__":
    FILE_PATH = "Iterators_and_generators/sample_file.txt"
    contents = read_file(file_name=FILE_PATH)
    for content in contents:
        print(content)
