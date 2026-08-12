"""Create a BankAccount with deposit and withdrawal."""

MIN_WITHDRAW_AMOUNT = 500


class BankAccount:
    """Represent a bank account."""

    def __init__(self, initial_balance: float = 0.0) -> None:
        self.__balance = initial_balance

    def get_account_balance(self) -> float:
        """Return the current bank account balance."""
        return self.__balance

    def deposit_amount(self, amount: float) -> None:
        """Deposit amount into the bank account."""
        if amount <= 0:
            raise ValueError("Deposit amount should be greater than zero.")
        self.__balance += amount

    def withdraw_amount(self, amount: float) -> None:
        """Withdraw amount from bank account balance."""
        if amount <= MIN_WITHDRAW_AMOUNT:
            raise ValueError(
                "Withdraw amount should be greater than "
                f"{MIN_WITHDRAW_AMOUNT}."
            )

        if (amount > self.get_account_balance()):
            raise ValueError("Insufficient bank account balance.")

        self.__balance -= amount


def main() -> None:
    """Run the main Program."""
    bank_account_object = BankAccount()
    while True:
        print("1. Current Account Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit.")
        try:
            choice = input("Enter your choice: ")

            if choice not in {"1", "2", "3", "4"}:
                print("Invalid choice. Please enter a valid choice(1-4).")

            elif choice == "4":
                print("Exit from operations.")
                break

            elif choice == "1":
                print(
                    "Current Account Balance: "
                    f"{bank_account_object.get_account_balance()}"
                )
            elif choice == "2":
                amount = float(input("Enter the deposit amount: "))
                bank_account_object.deposit_amount(amount=amount)

            elif choice == "3":
                amount = float(input("Enter the withdraw amount: "))
                bank_account_object.withdraw_amount(amount=amount)
        except ValueError as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")


if __name__ == "__main__":
    main()
