"""Person → Employee → Manager. Mult-level inheritance."""


class Person:
    """Represent a person."""
    def display_person_information(self) -> None:
        """Display person information."""
        print("Person information.")


class Employee(Person):
    """Represent an employee."""
    def display_employee_information(self) -> None:
        """Display employee information."""
        print("Display employee information.")


class Manager(Employee):
    """Represent a manager."""
    def display_manager_information(self) -> None:
        """Display manager information."""
        print("Display manager information.")


def main() -> None:
    """Run the main program."""
    manager_object = Manager()
    manager_object.display_person_information()
    manager_object.display_employee_information()
    manager_object.display_manager_information()


if __name__ == "__main__":
    main()
