"""
Account → SavingsAccount

Create:

    Account
    ↓
    SavingsAccount

Implement deposit and withdrawal.
"""

WITHDRAWAL_MULTIPLE = 100
MINIMUM_BALANCE = 1000


class Account:
    """Represent an account."""

    def __init__(self, account_number: int) -> None:
        self.account_number = account_number


class SavingsAccount(Account):
    """Represent a savings account."""

    def __init__(self, account_number: int, balance: float) -> None:
        super().__init__(account_number)
        if balance < 0:
            raise ValueError("Initial balance should not be negative.")
        self.__balance = balance

    def get_balance(self) -> float:
        """Return the account balance."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        """Deposit amount to the savings account."""
        if amount <= 0:
            raise ValueError("Deposit amount should be greater than zero.")

        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw amount from savings account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount should be greater than zero.")

        if amount % WITHDRAWAL_MULTIPLE != 0:
            raise ValueError(
                "Withdrawal amount should be a multiple of "
                f"{WITHDRAWAL_MULTIPLE}.")

        if self.__balance - amount < MINIMUM_BALANCE:
            raise ValueError("Minimum balance must be maintained.")

        self.__balance -= amount


def main() -> None:
    """Run the main program."""

    savings_account = SavingsAccount(account_number=101, balance=5000)

    while True:
        print("Bank Account Operations:")
        print("1. Get Account Balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice not in {"1", "2", "3", "4"}:
                print("Invalid choice. Please select a valid choice (1-4).")
            elif choice == "4":
                print("Exit from operations.")
                break
            elif choice == "1":
                print(f"Current Balance: {savings_account.get_balance()}")
            elif choice == "2":
                amount = float(input("Enter the amount: "))
                savings_account.deposit(amount=amount)
            elif choice == "3":
                amount = float(input("Enter the amount: "))
                savings_account.withdraw(amount=amount)

        except ValueError as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")


if __name__ == "__main__":
    main()
