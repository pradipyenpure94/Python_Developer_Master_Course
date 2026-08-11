"""__enter__() method."""


class EmployeeManager:
    """Represent an EmployeeManager."""

    def __enter__(self):
        print("Employee manager started...")
        return self

    def add_employee(self, name: str) -> None:
        """Add employee."""
        print(f"Add employee: {name}")

    def __exit__(self, exc_type, exc, tb):
        print("Employee manager closed...")


def main() -> None:
    """Return the main program."""
    with EmployeeManager() as manager:
        manager.add_employee("Pradip")


if __name__ == "__main__":
    main()
