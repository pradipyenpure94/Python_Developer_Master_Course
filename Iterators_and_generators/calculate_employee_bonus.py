"""Generator-based data pipeline."""

from collections.abc import Iterable, Iterator
from pathlib import Path


FILE_PATH = Path("Iterators_and_generators/sample_employee_data.csv")

MIN_EMPLOYEE_SALARY = 30000


def generate_employee_records(file_path: Path) -> Iterator[str]:
    """Generate employee records."""
    with open(file=file_path, mode="r", encoding="utf-8", newline="") as file:
        next(file, None)
        for record in file:
            yield record


def filter_employee_records(
    employee_records: Iterable[str]
) -> Iterator[str]:
    """Filter employee records who has salary greater than 30000."""
    for record in employee_records:
        try:
            salary = record.split(",")[3].strip()
            if float(salary) > MIN_EMPLOYEE_SALARY:
                yield record
        except (IndexError, ValueError):
            continue


def generate_employee_details(
    employee_records: Iterable[str]
) -> Iterator[dict[str, str | float]]:
    """Generate employee details."""
    for record in employee_records:
        try:
            record = record.split(",")
            employee_id = record[0]
            employee_name = record[1]
            employee_salary = float(record[3])
            employee_bonus = employee_salary * 0.10

            employee_data = {
                "id": employee_id,
                "name": employee_name.strip().upper(),
                "salary": employee_salary,
                "bonus": employee_bonus,
                "total_salary": employee_salary + employee_bonus,
            }

            yield employee_data

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    employee_iterator = generate_employee_records(file_path=FILE_PATH)
    filter_employee_iterator = filter_employee_records(
        employee_records=employee_iterator
    )
    employee_data_iterator = generate_employee_details(
        employee_records=filter_employee_iterator
    )

    for record in employee_data_iterator:
        print(record)
