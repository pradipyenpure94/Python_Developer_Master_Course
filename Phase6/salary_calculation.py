"""
Accept monthly salary and bonus. Displays the total annual compensations,
assuming the bonus is monthly.
"""

monthly_salary = float(input("Enter the monthly salary: "))
monthly_bonus = float(input("Enter the monthly bonus: "))

monthly_pay = monthly_salary + monthly_bonus
total_annual_compensations = monthly_pay * 12
print(f"Monthly Pay          : {monthly_pay:.2f}")
print(f"Annual Compensations : {total_annual_compensations:.2f}")
