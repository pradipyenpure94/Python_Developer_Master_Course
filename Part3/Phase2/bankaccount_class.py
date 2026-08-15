"""
Bank Account

Create a BankAccount class with:

    account number
    account holder
    balance

Implement:

    deposit()
    withdraw()
    display_balance()
"""

MIN_ACCOUNT_BALANCE = 5000


class BankAccount:
    """Represent a bank account."""

    def __init__(
        self,
        account_number: int,
        account_holder: str,
        balance: float
    ) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def get_account_balance(self) -> float:
        """Return the account balance."""
        return self.__balance

    def withdraw_amount(self, amount: float) -> None:
        """Withdraw amount from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.__balance - amount < MIN_ACCOUNT_BALANCE:
            raise ValueError("Insufficient Account Balance.")
        self.__balance -= amount

    def deposit_amount(self, amount: float) -> None:
        """Deposit amount to the bank account."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.__balance += amount


def main() -> None:
    """Run the main program."""
    bank_account = BankAccount(
        account_number=101,
        account_holder="Pradip",
        balance=0.0
    )

    while True:
        print("Bank Operations:")
        print("1. Check Account Balance")
        print("2. Withdraw Amount")
        print("3. Deposit Amount")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice not in {"1", "2", "3", "4"}:
                print("Invalid choice. Please enter a valid choice (1-4).")

            elif choice == "4":
                print("Exit from operations.")
                break

            elif choice == "1":
                print("Bank Account Balance Details:")
                print(f"Account Number  : {bank_account.account_number}")
                print(f"Account Holder  : {bank_account.account_holder}")
                print(
                    f"Account Balance : "
                    f"{bank_account.get_account_balance():.2f}"
                )

            elif choice == "2":
                amount = float(input("Enter the withdraw amount: "))
                bank_account.withdraw_amount(amount=amount)
                print(f"Account Number  : {bank_account.account_number}")
                print(f"Account Holder  : {bank_account.account_holder}")
                print(f"Withdraw Amount : {amount:.2f}")
                print(
                    f"Account Balance : "
                    f"{bank_account.get_account_balance():.2f}"
                )

            elif choice == "3":
                amount = float(input("Enter the deposit amount: "))
                bank_account.deposit_amount(amount=amount)
                print(f"Account Number  : {bank_account.account_number}")
                print(f"Account Holder  : {bank_account.account_holder}")
                print(f"Deposit Amount : {amount:.2f}")
                print(
                    f"Account Balance : "
                    f"{bank_account.get_account_balance():.2f}"
                )

        except ValueError as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")


if __name__ == "__main__":
    main()
