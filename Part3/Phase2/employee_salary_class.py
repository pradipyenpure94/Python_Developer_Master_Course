"""
Employee Salary

Create an Employee class with monthly salary.

Calculate:

    - annual salary
    - bonus
    - final salary
"""

MONTHS_IN_YEAR = 12
BONUS_PERCENTAGE = 10


class Employee:
    """Represent an employee."""
    def __init__(self, monthly_salary: float) -> None:
        if monthly_salary <= 0:
            raise ValueError("Monthly salary must be greater than zero.")

        self.monthly_salary = monthly_salary

    def get_annual_salary(self) -> float:
        """Return the annual salary."""
        return self.monthly_salary * MONTHS_IN_YEAR

    def get_bonus(self) -> float:
        """Return the annual bonus."""
        return self.get_annual_salary() * BONUS_PERCENTAGE / 100

    def get_final_salary(self) -> float:
        """Return the final salary."""
        return self.get_annual_salary() + self.get_bonus()


def main() -> None:
    """Run the main program."""
    try:
        monthly_salary = float(input("Enter the employee monthly salary: "))
        employee = Employee(monthly_salary=monthly_salary)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print("Employee Information: ")
        print(f"Monthly Salary  : {employee.monthly_salary:.2f}")
        print(f"Annual Salary   : {employee.get_annual_salary():.2f}")
        print(f"Bonus           : {employee.get_bonus():.2f}")
        print(f"Final Salary    : {employee.get_final_salary():.2f}")


if __name__ == "__main__":
    main()
