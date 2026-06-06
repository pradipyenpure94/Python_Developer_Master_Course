"""Nested lambda function."""


def tax_calculator(tax: float, amount: float) -> float:
    """
    Return the total amount including tax.

    Args:
        tax (float): Tax percentage.
        amount (float): Original amount.

    Returns:
        float: Total amount including tax.
    """
    total_amount = lambda rate: lambda amt: amt + ((rate / 100) * amt)
    return total_amount(tax)(amount)


if __name__ == "__main__":
    try:
        tax = float(input("Enter tax percentage: "))
        amount = float(input("Enter an amount: "))
        result = tax_calculator(tax=tax, amount=amount)
        print(f"Total amount including tax: {result}")
    except ValueError:
        print("Invalid input! Please enter a number.")
