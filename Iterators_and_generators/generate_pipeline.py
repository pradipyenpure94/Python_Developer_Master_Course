"""Custom Generator-Based Data Processor."""

from collections.abc import Generator, Iterable, Iterator


def generate_employees_data(data: Iterable[dict]) -> Generator[dict]:
    """Generate the employees data."""
    for employee in data:
        yield employee


def generate_salary_filtered_employees(
    data: Iterator[dict],
    salary: float
) -> Generator[dict]:
    """Generate the salary filter generator."""
    for employee in data:
        if employee['salary'] > salary:
            yield employee


def generate_employee_names(data: Iterator[dict]) -> Generator[str]:
    """Generate the employee name."""
    for employee in data:
        yield employee["name"]


if __name__ == "__main__":
    employees = [
        {"name": "Amit", "salary": 45000},
        {"name": "Rahul", "salary": 65000},
        {"name": "Sneha", "salary": 75000},
        {"name": "Priya", "salary": 50000},
    ]

    employee_data = generate_employees_data(data=employees)
    salary_filtered_employees = generate_salary_filtered_employees(
        data=employee_data,
        salary=50000
    )

    employee_names = generate_employee_names(data=salary_filtered_employees)

    for name in employee_names:
        print(name)
