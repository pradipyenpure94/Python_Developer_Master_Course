"""__exit__() method."""


class DatabaseConnection:
    """Represent a DatabaseConnection."""
    def __enter__(self) -> "DatabaseConnection":
        print("Database connection started...")
        return self

    def add_employee(self, name: str) -> None:
        """Add the employee."""
        print(f"Add employee: {name}")

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        print(f"Exception Type: {exc_type}")
        print(f"Exception: {exc}")
        print(f"Trace back: {tb}")
        print("Database connection closed...")


def main() -> None:
    """Run the main program."""
    with DatabaseConnection() as db_obj:
        db_obj.add_employee(name="Amit")
        db_obj.add_employee(name="Pradip")


if __name__ == "__main__":
    main()
