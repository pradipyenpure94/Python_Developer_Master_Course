"""Calculate an employee's annual salary from monthly salary."""

try:
    # Accept monthly salary input from user
    salary = float(input("Enter the monthly salary: "))
    if salary <= 0:
        raise ValueError("Salary must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
else:
    annual_salary = salary * 12
    print(f"Employee Annual Salary: {annual_salary:.2f}")
