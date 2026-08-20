"""
Employee Management System

Create:

    Employee
    ├── Developer
    ├── Tester
    └── Manager

Implement:

    employee information
    salary calculation
    role-specific behavior
    employee count
    salary validation

Use:

    Encapsulation
    Inheritance
    Polymorphism
    Method overriding
    Class variables
    super()
"""

DEVELOPER_ALLOWANCE = 0.10
TESTER_ALLOWANCE = 0.50
MANAGER_BONUS = 0.20

MIN_SALARY = 15000
MAX_SALARY = 500000


class Employee:
    """Represent an employee."""

    employee_count = 0

    def __init__(self, employee_id: int, name: str, salary: float) -> None:
        self.employee_id = employee_id
        self.name = name
        self.__salary = self.validate_salary(salary=salary)
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls) -> int:
        """Return the employee count."""
        return cls.employee_count

    @staticmethod
    def validate_salary(salary: float) -> float:
        """Validate and return the salary."""
        if not isinstance(salary, (int, float)):
            raise TypeError("Salary must be a number.")

        if not MIN_SALARY <= salary <= MAX_SALARY:
            raise ValueError(
                f"Employee salary must be between {MIN_SALARY} "
                f"and {MAX_SALARY}."
            )
        return float(salary)

    def get_salary(self) -> float:
        """Return the employee salary."""
        return self.__salary

    def calculate_salary(self) -> float:
        """Return the employee salary."""
        return self.__salary

    def work(self) -> str:
        """Return the employee general work behaviour."""
        return "Employee is working."

    def display_information(self) -> None:
        """Display employee information."""
        print("-" * 40)
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : {self.calculate_salary():.2f}")
        print(f"Work        : {self.work()}")
        print("-" * 40)


class Developer(Employee):
    """Represent a developer."""

    def __init__(
        self,
        employee_id: int,
        name: str,
        salary: float,
        programming_language: str
    ) -> None:
        super().__init__(employee_id=employee_id, name=name, salary=salary)
        self.programming_language = programming_language

    def calculate_salary(self) -> float:
        """Return the developer salary with technical allowance."""
        basic_salary = self.get_salary()
        technical_allowance = basic_salary * DEVELOPER_ALLOWANCE
        return basic_salary + technical_allowance

    def work(self) -> str:
        """Return the developer-specific behaviour."""
        return f"Developing software using {self.programming_language}."


class Tester(Employee):
    """Represent a tester."""

    def __init__(
        self,
        employee_id: int,
        name: str,
        salary: float,
        testing_tool: str
    ) -> None:
        super().__init__(employee_id=employee_id, name=name, salary=salary)
        self.testing_tool = testing_tool

    def calculate_salary(self) -> float:
        """Calculate and return the tester salary with testing allowance."""
        basic_salary = self.get_salary()
        testing_allowance = basic_salary * TESTER_ALLOWANCE
        return basic_salary + testing_allowance

    def work(self) -> str:
        """Return tester-specific behaviour."""
        return f"Testing software using {self.testing_tool}."


class Manager(Employee):
    """Represent a manager."""

    def __init__(
        self,
        employee_id: int,
        name: str,
        salary: float,
        team_size: int
    ) -> None:
        super().__init__(employee_id=employee_id, name=name, salary=salary)
        self.team_size = team_size

    def calculate_salary(self) -> float:
        """Return the calculated salary with management bonus."""
        basic_salary = self.get_salary()
        management_bonus = basic_salary * MANAGER_BONUS
        return basic_salary + management_bonus

    def work(self) -> str:
        """Return manager specific behaviour."""
        return f"Managing a team of {self.team_size} employees."


def main() -> None:
    """Run the employee management system."""
    try:
        developer = Developer(
            employee_id=101,
            name="Pradip",
            salary=20000,
            programming_language="Python"
        )

        tester = Tester(
            employee_id=102,
            name="Ajay",
            salary=20000,
            testing_tool="Selenium"
        )

        manager = Manager(
            employee_id=103,
            name="Kedar",
            salary=40000,
            team_size=5
        )

        employees: list[Employee] = [developer, tester, manager]

        print("\nEmployee Information:")
        for employee in employees:
            employee.display_information()
        print(
            f"Total Employee: {Employee.get_employee_count()}"
        )
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
