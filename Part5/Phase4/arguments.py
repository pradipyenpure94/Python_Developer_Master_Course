"""Function using both **args and **kwargs."""


def display_employee_information(*emp_names: str, **salary_components: float) -> None:
    """Display Employee Information."""
    print("Employee Information:")
    print(f"Employee Name : {emp_names[0] if emp_names else ''}")
    print(f"HRA           : {salary_components['HRA']:.2f}")
    print(f"DA            : {salary_components['DA']:.2f}")
    print(f"DB            : {salary_components['DB']:.2f}")


if __name__ == "__main__":
    display_employee_information("Pradip Yenpure", HRA=1500, DA=450, DB=2500)
