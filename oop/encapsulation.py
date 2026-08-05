"""Introduction to encapsulation."""


class BankAccount:
    """Bank account transactions."""
    def __init__(self, balance):
        self.__balance = balance

    def deposit_amount(self, amount):
        """Deposit amount"""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount

    def withdraw_amount(self, amount):
        """Withdraw amount"""
        if amount <= 0:
            print("Withdraw amount must be positve.")
            return
        if amount > self.__balance:
            print("Insufficient balance.")
            return
        self.__balance -= amount

    def get_balance(self):
        """Return the account balance."""
        return self.__balance


class Employee:
    """Subclass"""
    account = BankAccount(5)
    account.deposit_amount(amount=450)
    account.withdraw_amount(amount=5)
    print(account.get_balance())
