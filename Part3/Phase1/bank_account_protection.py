"""Bank account balance protection using private variable."""


class BankAccount:
    """Represent a bank bccount."""

    def __init__(self, balance: float) -> None:
        self.__balance = balance

    def get_account_balance(self) -> float:
        """Return the account balance."""
        return self.__balance


def main() -> None:
    """Run the main program."""
    bank_account_obj = BankAccount(balance=5000)
    print(f"Bank account balance: {bank_account_obj.get_account_balance()}")


if __name__ == "__main__":
    main()
