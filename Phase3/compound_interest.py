"""Calculate compound interest."""


def calculate_compound_interest(principal: float, rate: float, time: float,
                                compound_frequency: int) -> float:
    """
    Return the compound interest amount.

    Args:
        principal (float): Principal amount.
        rate (float): Rate of interest in percent (%).
        time (float): Time in years.
        compound_frequency (int): Number of compounding periods per year.

    Returns:
        float: Calculated compound interest amount (CI).
    """
    # Convert rate of interest into decimal
    r = rate / 100

    if compound_frequency <= 0:
        raise ValueError("Compound frequecy must be greater than zero.")

    # Maturity amount
    total_amount = principal * ((1 + (r / compound_frequency)) ** (
        compound_frequency * time))
    compound_interest = total_amount - principal
    return compound_interest


if __name__ == "__main__":
    try:
        amount = float(input("Enter principal amount: "))
        rate_in_percent = float(input("Enter percentage amount: "))
        time_in_years = float(input("Enter period in years: "))
        compound_freq = int(input("Enter compound interest frequency per year:"))
        result = calculate_compound_interest(principal=amount,
                                             rate=rate_in_percent,
                                             time=time_in_years,
                                             compound_frequency=compound_freq)
        print(f"Compound interest amount: {result}")
    except ValueError as error:
        print(f"Error: {error}")
