"""
1. Create Employee with private salary.
2. Create getter and setter methods.
"""


class Employee:
    """Represent an employee."""

    def __init__(self, salary: float) -> None:
        self.__salary = salary

    def get_employee_salary(self) -> float:
        """Return the employee salary."""
        return self.__salary

    def set_employee_salary(self, salary: float) -> None:
        """Update employee salary."""
        self.__salary = salary


employee_obj = Employee(salary=5000)
print(f"Current Employee Salary: {employee_obj.get_employee_salary()}")
employee_obj.set_employee_salary(salary=4500)
print(f"Current Employee Salary: {employee_obj.get_employee_salary()}")
employee_obj.set_employee_salary(salary=9500)
print(f"Current Employee Salary: {employee_obj.get_employee_salary()}")
