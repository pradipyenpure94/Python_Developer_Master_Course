"""Create custom exception for insufficient bank balance."""


class InsufficientBankBalance(Exception):
    """Custom exception for insufficient bank balance."""


ACCOUNT_BALANCE = 1000

try:
    withdraw_amount = float(input("Enter the withdrawal amount: "))
    if withdraw_amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if withdraw_amount > ACCOUNT_BALANCE:
        raise InsufficientBankBalance("Insufficient account balance.")
except (ValueError, InsufficientBankBalance) as error:
    print(f"Error: {error}")
else:
    print(f"Withdrawn amount: {withdraw_amount:.2f}")
