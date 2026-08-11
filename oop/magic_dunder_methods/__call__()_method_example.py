"""__call__() method."""


class Employee:
    """Represent an employee."""

    def __call__(self, basic_salary: float, emp_bonus: float) -> float:
        return basic_salary + emp_bonus


def main() -> None:
    """Run the main program."""
    emp_object = Employee()
    total_salary = emp_object(basic_salary=100000, emp_bonus=50000)
    print(f"Total salary: {total_salary:.2f}")


if __name__ == "__main__":
    main()
