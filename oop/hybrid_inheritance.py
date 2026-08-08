"""Hybrid inheritance."""


class Employee:
    """Represent an employee."""
    def __init__(self, emp_name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.emp_name = emp_name

    def display_employee_information(self) -> None:
        """Display the employee information."""
        print(f"Employee Name         : {self.emp_name}")


class Developer(Employee):
    """Represent a developer."""
    def __init__(self, emp_name: str, course_name: str, **kwargs) -> None:
        super().__init__(emp_name=emp_name, **kwargs)
        self.course_name = course_name

    def display_developer_information(self) -> None:
        """Display the developer information."""
        print(f"Course Name           : {self.course_name}")


class Tester(Employee):
    """Represent a tester."""
    def __init__(self, emp_name: str, module_name: str, **kwargs) -> None:
        super().__init__(emp_name=emp_name, **kwargs)
        self.module_name = module_name

    def display_tester_information(self) -> None:
        """Display the tester information."""
        print(f"Module Name           : {self.module_name}")


class TechnicalLead(Developer, Tester):
    """Represent a technical lead."""
    def __init__(
        self,
        emp_name: str,
        course_name: str,
        module_name: str,
        programming_language: str,
        **kwargs
    ) -> None:
        super().__init__(
            emp_name=emp_name,
            course_name=course_name,
            module_name=module_name,
            **kwargs
        )
        self.programming_language = programming_language

    def display_technical_lead_information(self) -> None:
        """Display the technical lead information."""
        print(f"Programming Language  : {self.programming_language}")


def main() -> None:
    """Run the main program."""
    technical_lead_obj = TechnicalLead(
        emp_name="Pradip Yenpure",
        course_name="Python",
        module_name="Sales",
        programming_language="Python"
    )
    print("-" * 40)
    print("Technical Lead Information:")
    print("-" * 40)
    technical_lead_obj.display_employee_information()
    technical_lead_obj.display_developer_information()
    technical_lead_obj.display_tester_information()
    technical_lead_obj.display_technical_lead_information()


if __name__ == "__main__":
    main()
