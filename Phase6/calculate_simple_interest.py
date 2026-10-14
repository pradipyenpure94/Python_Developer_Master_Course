"""Calculate simple interest and total amount from principal, rate and time."""

try:
    principal = float(input("Enter the principal amount         : "))
    rate_of_interest = float(input("Enter the rate of interest         : "))
    time_years = float(input("Enter the time duration (in years) : "))
    if principal < 0 or rate_of_interest < 0:
        raise ValueError(
            "Principal amount and interest rate cannot be negative."
        )
    if time_years <= 0:
        raise ValueError(
            "Time duration must be greater than zero."
        )
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    interest_amount = principal * rate_of_interest * time_years / 100
    print(f"Interest amount                    : {interest_amount:.2f}")
    total_amount = principal + interest_amount
    print(f"Total amount                       : {total_amount:.2f}")
