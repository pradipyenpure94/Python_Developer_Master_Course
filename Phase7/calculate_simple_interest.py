"""Calculate simple interest."""

principal_amount = float(input("Enter the principal amount: "))
period = float(input("Enter the period in years: "))
rate_of_interest = float(input("Enter the rate of interest: "))
interest_amount = principal_amount * rate_of_interest * period / 100
print(f"Interest Amount: {interest_amount:.2f}")
