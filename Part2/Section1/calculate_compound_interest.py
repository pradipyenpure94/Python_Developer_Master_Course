"""Calculate compound interest."""

try:
    # Principal amount validation
    principal_amount = float(input("Enter the principal amount: "))
    if principal_amount <= 0:
        raise ValueError("Principal amount must be greater than zero.")

    # Interest rate validation
    interest_rate = float(input("Enter the rate of interest: "))
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    # Time period validation
    time_period = float(input("Enter the duration (in years): "))
    if time_period <= 0:
        raise ValueError("Time period must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    amount = principal_amount * (1 + interest_rate / 100) ** time_period
    compound_interest = amount - principal_amount
    print(f"Compound interest: {compound_interest:.2f}")
finally:
    print("Operation completed.")
