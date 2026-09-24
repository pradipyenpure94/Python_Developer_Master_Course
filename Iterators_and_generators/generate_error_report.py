"""Mini Project: Memory-Efficient Log Processor."""


from collections.abc import Iterable, Iterator
from pathlib import Path

FILE_PATH = Path("Iterators_and_generators/error_log_data.txt")


def generate_log_lines(file_path: Path) -> Iterator[str]:
    """Generate log lines."""
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            yield line


def filter_error_logs(errors: Iterable[str]) -> Iterator[str]:
    """Generate only ERROR log lines."""
    for error in errors:
        if error.startswith("ERROR"):
            yield error.strip()


def extract_error_messages(errors: Iterable[str]) -> Iterator[str]:
    """Extract messages from ERROR log lines."""
    for error in errors:
        try:
            _, message = error.split(maxsplit=1)
            yield message
        except ValueError:
            continue


if __name__ == "__main__":
    log_lines = generate_log_lines(file_path=FILE_PATH)
    error_logs = filter_error_logs(errors=log_lines)
    error_messages = extract_error_messages(
        errors=error_logs
    )

    error_count = 0

    for message in error_messages:
        print(message)
        error_count += 1

    print(f"\nCount Errors: {error_count}")
