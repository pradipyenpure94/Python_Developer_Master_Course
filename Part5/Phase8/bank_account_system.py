"""Build a complete encapsulated Bank Account System."""

MIN_DEPOSIT_AMOUNT = 1
MIN_WITHDRAW_AMOUNT = 1
MIN_ACCOUNT_BALANCE = 100


class InsufficientBalanceError(Exception):
    """Custom exception insufficient account balance."""


class MinimumBalanceError(Exception):
    """Custom exception for minimum account balance."""


class BankAccount:
    """Represent a bank account."""
    total_accounts = 0

    def __init__(
        self,
        account_holder: str,
        balance: float
    ) -> None:
        if balance < MIN_ACCOUNT_BALANCE:
            raise ValueError(
                f"Initial balance must be at least "
                f"{MIN_ACCOUNT_BALANCE:.2f}."
            )
        BankAccount.total_accounts += 1
        self.__account_number = f"Acc{BankAccount.total_accounts:04d}"
        self.__account_holder = account_holder.strip()
        self.__balance = balance
        self.__transactions: list[str] = []

    def get_account_number(self) -> str:
        """Return the account number."""
        return self.__account_number

    def get_account_holder(self) -> str:
        """Return the account holder name."""
        return self.__account_holder

    def get_account_balance(self) -> float:
        """Return the account balance."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        if amount < MIN_DEPOSIT_AMOUNT:
            raise ValueError(
                f"Deposit amount at least {MIN_DEPOSIT_AMOUNT:.2f}."
            )
        self.__balance += amount
        self.__transactions.append(f"Deposited {amount:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from bank account."""
        if amount < MIN_WITHDRAW_AMOUNT:
            raise ValueError(
                f"Withdraw amount at least {MIN_WITHDRAW_AMOUNT:.2f}"
            )
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient account balance.")

        remaining_balance = self.__balance - amount
        if remaining_balance < MIN_ACCOUNT_BALANCE:
            raise MinimumBalanceError(
                f"Minimum account balance {MIN_ACCOUNT_BALANCE:.2f} "
                f"must be maintained.")
        self.__balance = remaining_balance
        self.__transactions.append(f"Withdrawn {amount:.2f}")

    def get_transactions_history(self) -> tuple[str, ...]:
        """Return the transactions history."""
        return tuple(self.__transactions)

    def display_account_summary(self) -> None:
        """Return transactions history."""
        print("\n----Account Summary----")
        print(f"Account Number  : {self.__account_number}")
        print(f"Account Holder  : {self.__account_holder}")
        print(f"Account Balance : {self.__balance}")
        print("-" * 30)


def main() -> None:
    """Run the Bank Account System."""
    try:
        bank_account_obj = BankAccount(account_holder="Pradip", balance=500)
        bank_account_obj.deposit(amount=4500)
        bank_account_obj.withdraw(amount=1000)

        print("\nTransactions History:")
        for transaction in bank_account_obj.get_transactions_history():
            print(transaction)
    except (
        InsufficientBalanceError,
        MinimumBalanceError,
        ValueError
    ) as error:
        print(f"Error: {error}")
    else:
        bank_account_obj.display_account_summary()


if __name__ == "__main__":
    main()
