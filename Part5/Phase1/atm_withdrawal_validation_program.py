"""Create a simple ATM withdrawal validation program."""

WITHDRAWAL_DENOMINATION = 100
DAILY_WITHDRAW_LIMIT = 10000
ACCOUNT_BALANCE = 50000


try:
    amount = int(input("Enter the withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if not amount % WITHDRAWAL_DENOMINATION == 0:
        raise ValueError(
            f"Amount must be a multiple of {WITHDRAWAL_DENOMINATION}."
        )
    if amount > DAILY_WITHDRAW_LIMIT:
        raise ValueError("Withdraw limit exceeded.")
    if amount > ACCOUNT_BALANCE:
        raise ValueError("Insufficient account balance.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    ACCOUNT_BALANCE -= amount
    print(f"{amount} withdrawn successfully.")
    print(f"Current Balance: {ACCOUNT_BALANCE}")
