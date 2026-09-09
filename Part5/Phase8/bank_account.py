"""Create BankAccount with private balance."""


class BankAccount:
    """Represent a Bank Account."""

    def __init__(self, balance: float) -> None:
        self.__balance = balance


bank_account_obj = BankAccount(balance=5000)
