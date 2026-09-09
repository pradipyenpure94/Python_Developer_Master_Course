"""
1. Create BankAccount with private balance.
2. Implement deposit operation.
"""


class BankAccount:
    """Represent a Bank Account."""

    def __init__(self, balance: float) -> None:
        self.__balance = balance

    def deposit_amount(self, amount: float) -> None:
        """Deposit amount in Bank Account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount

    def get_account_balance(self) -> float:
        """Return the account balance."""
        return self.__balance


bank_account_obj = BankAccount(balance=5000)
bank_account_obj.deposit_amount(amount=500)
print(f"Current Balance: {bank_account_obj.get_account_balance()}")
