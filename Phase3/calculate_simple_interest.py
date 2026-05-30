"""Calculate simple interest."""


def calculate_interest(principal: float, rate: float, time: float) -> float:
    """
    Return the simple interest amount.

    Args:
        principal (float): Principal amount.
        rate (float): Rate of interest in percent (%).
        time (float): Time in years.

    Returns:
        float: Return the interest amount.
    """

    interest_amount = (principal * rate * time) / 100
    return interest_amount


if __name__ == "__main__":
    try:
        principal_amount = float(input("Enter principal amount: "))
        rate_in_percent = float(input("Enter rate of interest (%): "))
        time_in_years = float(input("Enter duration in years: "))
        interest_amt = calculate_interest(principal=principal_amount,
                                          rate=rate_in_percent,
                                          time=time_in_years)
        print(f"Interest amount: {interest_amt}")
    except ValueError:
        print("Invalid input! Please enter a number.")
