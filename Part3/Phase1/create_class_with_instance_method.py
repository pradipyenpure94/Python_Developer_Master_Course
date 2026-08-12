"""Create a BankAccount class with instance methods."""


class BankAccount:
    """Represent a bank account."""
    def __init__(self, account_holder_name: str, account_number: int) -> None:
        self.account_number = account_number
        self.account_holder_name = account_holder_name

    def display_account_information(self) -> None:
        """Display the account information."""
        print("-" * 50)
        print("Bank Account Holder Information:")
        print("-" * 50)
        print(f"\u25aa Bank Account Number: {self.account_number}")
        print(f"\u25aa Bank Account Holder Name: {self.account_holder_name}")


def main() -> None:
    """Run the main program."""
    bank_account_object = BankAccount(
        account_number=101020304568,
        account_holder_name="Pradip Rajendra Yenpure"
    )

    bank_account_object.display_account_information()


if __name__ == "__main__":
    main()
