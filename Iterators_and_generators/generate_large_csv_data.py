"""
Generate for processing large CSV data.
Concept:
        CSV
        |
        Read one row
        |
        Validate
        |
        Transform
        |
        Output
"""
import csv
from collections.abc import Iterator
from pathlib import Path

FILE_PATH = Path("Iterators_and_generators/sample_employee_data.csv")

MIN_EMPLOYEE_AGE = 18


def process_employee_data(
    file_path: Path
) -> Iterator[dict[str, int | str]]:
    """Read, validate, transform, and generate employee records."""
    with open(
        file=file_path,
        mode="r",
        encoding="utf-8",
        newline="",
    ) as file:
        for row in csv.DictReader(file):
            if not row["id"]:
                continue

            if not row["name"]:
                continue

            try:
                employee_id = int(row["id"])
                employee_age = int(row["age"])
            except ValueError:
                continue

            if employee_age < MIN_EMPLOYEE_AGE:
                continue

            processed_data = {
                "id": employee_id,
                "name": row["name"].strip().upper(),
                "age": employee_age,
            }
            yield processed_data


if __name__ == "__main__":
    iterator = process_employee_data(file_path=FILE_PATH)
    for record in iterator:
        print(record)
