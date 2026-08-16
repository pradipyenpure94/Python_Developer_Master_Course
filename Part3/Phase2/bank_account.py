"""
Secure Bank Account

Make the balance private.

Provide:

    deposit()
    withdraw()
    get_balance()

    Prevent direct modification of balance.
"""

MIN_ACCOUNT_BALANCE = 500


class BankAccount:
    """Represent a bank account."""

    def __init__(self, initial_balance: float = 0.0) -> None:
        if initial_balance < MIN_ACCOUNT_BALANCE:
            raise ValueError(
                f"Initial balance must be at least {MIN_ACCOUNT_BALANCE}."
            )
        self.__balance = initial_balance

    def get_balance(self) -> float:
        """Return the bank account balance."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        """Deposit amount to the bank account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw amount from the account."""
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")

        if self.__balance - amount < MIN_ACCOUNT_BALANCE:
            raise ValueError("Minimum account balance must be maintained.")

        self.__balance -= amount


def main() -> None:
    """Run the main program."""
    try:
        bank_account = BankAccount(initial_balance=500)
        print(
            "Current Account Balance: "
            f"{bank_account.get_balance():.2f}"
        )
        bank_account.deposit(amount=500)
        print(
            "Current Account Balance: "
            f"{bank_account.get_balance():.2f}"
        )
        bank_account.withdraw(amount=100)
        print(
            "Current Account Balance: "
            f"{bank_account.get_balance():.2f}"
        )

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
