"""Calculate simple interest."""

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
    interest_amount = (principal_amount * interest_rate * time_period) / 100
    print(f"Interest amount: {interest_amount:.2f}")
finally:
    print("Operation completed.")
