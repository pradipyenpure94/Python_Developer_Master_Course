"""Example of method overriding."""

from colorama import Style

EMPLOYEE_BONUS_PERCENTAGE = 5
DEVELOPER_BONUS_PERCENTAGE = 10
MANAGER_BONUS_PERCENTAGE = 15


class Employee:
    """Represent an employee."""
    company_name = "Odoo"

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def calculate_bonus(self) -> float:
        """Calculate and return the employee salary bonus."""
        return self.salary * EMPLOYEE_BONUS_PERCENTAGE / 100

    def calculate_salary(self) -> float:
        """Calculate and return the employee total salary."""
        return self.salary + self.calculate_bonus()

    def display_employee_information(self) -> None:
        """Display the employee information."""
        print(f"Company Name             : {self.company_name}")
        print(f"Employee Name            : {self.name}")
        print(f"Employee Basic Salary    : {self.salary:.2f}")
        print(
            f"Employee Bonus ({EMPLOYEE_BONUS_PERCENTAGE}%)      : "
            f"{self.calculate_bonus():.2f}")
        print(f"Employee Total Salary    : {self.calculate_salary():.2f}")


class Developer(Employee):
    """Represent a developer."""
    def __init__(self, name: str, salary: float) -> None:
        super().__init__(name, salary)

    def calculate_bonus(self) -> float:
        """Calculate and return the developer bonus."""
        return self.salary * DEVELOPER_BONUS_PERCENTAGE / 100

    def display_developer_information(self) -> None:
        """Display the developer information."""
        print(f"Company Name             : {self.company_name}")
        print(f"Developer Name           : {self.name}")
        print(f"Developer Basic Salary   : {self.salary:.2f}")
        print(
            f"Developer Bonus ({DEVELOPER_BONUS_PERCENTAGE}%)    : "
            f"{self.calculate_bonus():.2f}")
        print(f"Developer Total Salary   : {self.calculate_salary():.2f}")


class Manager(Employee):
    """Represent a manager."""

    def __init__(self, name: str, salary: float) -> None:
        super().__init__(name, salary)

    def calculate_bonus(self) -> float:
        """Calculate and return the manager bonus."""
        return self.salary * MANAGER_BONUS_PERCENTAGE / 100

    def display_manager_information(self) -> None:
        """Display the manager information."""
        print(f"Company Name             : {self.company_name}")
        print(f"Manager Name             : {self.name}")
        print(f"Manager Basic Salary     : {self.salary:.2f}")
        print(
            f"Manager Bonus ({MANAGER_BONUS_PERCENTAGE}%)      : "
            f"{self.calculate_bonus():.2f}")
        print(f"Manager Total Salary     : {self.calculate_salary():.2f}")


def main() -> None:
    """Run the main program."""
    employee_obj = Employee(name="Amit", salary=75000)
    developer_obj = Developer(name="Pradip", salary=150000)
    manager_obj = Manager(name="Darshan", salary=250000)

    print("-" * 50)
    print(Style.BRIGHT + "Employee Information:" + Style.RESET_ALL)
    employee_obj.display_employee_information()
    print("-" * 50)
    print(Style.BRIGHT + "Developer Information:" + Style.RESET_ALL)
    developer_obj.display_developer_information()
    print("-" * 50)
    print(Style.BRIGHT + "Manager Information:" + Style.RESET_ALL)
    manager_obj.display_manager_information()
    print("-" * 50)


if __name__ == "__main__":
    main()
