"""
Mini Banking Management System using OOP.

Concepts demonstrated:
    - Encapsulation
    - Inheritance
    - Polymorphism
    - Abstraction
    - Exception handling
    - Input validation
    - Customer exceptions
    - Deposit
    - Withdrawal
    - Transfer
    - Balance checking
    - Transaction history
    - __str__
    - __repr__
    - __eq__
    - Class methods
    - Static methods
    """


from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


# ============================================================
# Custom Exceptions
# ============================================================


class BankingError(Exception):
    """Base exception for banking-related errors."""


class InvalidCustomerError(BankingError):
    """Raised when customer data is invalid."""


class CustomerNotFoundError(BankingError):
    """Raised when a customer cannot be found."""


class AccountNotFoundError(BankingError):
    """Raised when an account cannot be found."""


class InvalidAmountError(BankingError):
    """Raised when an invalid amount is provided."""


class InsufficientBalanceError(BankingError):
    """Raised when an account has insufficient balance."""


class MinimumBalanceError(BankingError):
    """Raised when minimum balance requirements are violated."""


class SameAccountTransferError(BankingError):
    """Raised when transferring to the same account."""


    # ============================================================
    # Transaction
    # ============================================================


@dataclass(frozen=True)
class Transaction:
    """Represent a banking transaction."""

    transaction_type: str
    amount: float
    account_number: str
    timestamp: str

    def __str__(self) -> str:
        """Return a user-friendly transaction representation."""
        return (
            f"{self.timestamp} | "
            f"{self.transaction_type:<10} | "
            f"₹{self.amount:,.2f}"
        )

    def __repr__(self) -> str:
        """Return a developer-friendly transaction representation."""
        return (
            f"Transaction("
            f"transaction_type={self.transaction_type!r}, "
            f"amount={self.amount!r}, "
            f"account_number={self.account_number!r}, "
            f"timestamp={self.timestamp!r})"
        )


# ============================================================
# Customer
# ============================================================


class Customer:
    """Represent a bank customer."""

    total_customers = 0

    def __init__(
        self,
        customer_id: int,
        name: str,
        email: str,
        phone: str,
    ) -> None:
        if not self.is_valid_name(name):
            raise InvalidCustomerError("Customer name cannot be empty.")

        if not self.is_valid_email(email):
            raise InvalidCustomerError("Invalid email address.")

        if not self.is_valid_phone(phone):
            raise InvalidCustomerError("Phone number must contain 10 digits.")

        self.customer_id = customer_id
        self.name = name.strip()
        self.email = email.strip()
        self.phone = phone.strip()

        self._accounts: list[BankAccount] = []

        Customer.total_customers += 1

    # --------------------------------------------------------
    # Static Methods
    # --------------------------------------------------------

    @staticmethod
    def is_valid_name(name: str) -> bool:
        """Validate customer name."""
        return isinstance(name, str) and bool(name.strip())

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate customer email."""
        return (
            isinstance(email, str)
            and "@" in email
            and "." in email.split("@")[-1]
        )

    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        """Validate customer phone number."""
        return (
            isinstance(phone, str)
            and phone.isdigit()
            and len(phone) == 10
        )

    # --------------------------------------------------------
    # Class Method
    # --------------------------------------------------------

    @classmethod
    def get_total_customers(cls) -> int:
        """Return the total number of customers."""
        return cls.total_customers

    # --------------------------------------------------------
    # Account Management
    # --------------------------------------------------------

    def add_account(self, account: "BankAccount") -> None:
        """Add an account to the customer."""
        self._accounts.append(account)

    def get_accounts(self) -> tuple["BankAccount", ...]:
        """Return customer accounts as an immutable tuple."""
        return tuple(self._accounts)

    # --------------------------------------------------------
    # Dunder Methods
    # --------------------------------------------------------

    def __str__(self) -> str:
        """Return a user-friendly customer representation."""
        return f"{self.customer_id} - {self.name}"

    def __repr__(self) -> str:
        """Return a developer-friendly customer representation."""
        return (
            f"Customer("
            f"customer_id={self.customer_id!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r}, "
            f"phone={self.phone!r})"
            )

    def __eq__(self, other: object) -> bool:
        """Compare customers using customer ID."""
        if not isinstance(other, Customer):
            return NotImplemented

        return self.customer_id == other.customer_id


# ============================================================
# Abstract BankAccount
# ============================================================


class BankAccount(ABC):
    """Represent an abstract bank account."""

    total_accounts = 0

    def __init__(
        self,
        account_number: str,
        customer: Customer,
        initial_balance: float = 0.0,
    ) -> None:
        self.account_number = account_number
        self.customer = customer
        self._balance = 0.0
        self._transactions: list[Transaction] = []

        self._validate_amount(initial_balance)

        if initial_balance > 0:
            self._balance = initial_balance
            self._add_transaction(
                transaction_type="DEPOSIT",
                amount=initial_balance,
            )

        BankAccount.total_accounts += 1

        # --------------------------------------------------------
        # Abstract Methods
        # --------------------------------------------------------

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw money according to account-specific rules."""

    # --------------------------------------------------------
    # Static Methods
    # --------------------------------------------------------

    @staticmethod
    def _validate_amount(amount: float) -> None:
        """Validate transaction amount."""
        if isinstance(
            amount, bool) or not isinstance(amount, (int, float)
                                            ):
            raise InvalidAmountError(
                "Amount must be a number."
            )

        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

    # --------------------------------------------------------
    # Common Account Operations
    # --------------------------------------------------------

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        self._validate_amount(amount)

        self._balance += amount

        self._add_transaction(
            transaction_type="DEPOSIT",
            amount=amount,
        )

    def transfer(self, amount: float, target: "BankAccount") -> None:
        """Transfer money to another account."""
        self._validate_amount(amount)

        if self == target:
            raise SameAccountTransferError(
                "Cannot transfer money to the same account."
            )

        self.withdraw(amount)
        target.deposit(amount)

        self._add_transaction(
            transaction_type="TRANSFER OUT",
            amount=amount,
        )

        target._add_transaction(
            transaction_type="TRANSFER IN",
            amount=amount,
        )

    def check_balance(self) -> float:
        """Return the current account balance."""
        return self._balance

    def get_transaction_history(
        self,
    ) -> tuple[Transaction, ...]:
        """Return immutable transaction history."""
        return tuple(self._transactions)

    # --------------------------------------------------------
    # Internal Transaction Method
    # --------------------------------------------------------

    def _add_transaction(
        self,
        transaction_type: str,
        amount: float,
    ) -> None:
        """Add a transaction to account history."""
        transaction = Transaction(
            transaction_type=transaction_type,
            amount=amount,
            account_number=self.account_number,
            timestamp=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

        self._transactions.append(transaction)

    # --------------------------------------------------------
    # Class Method
    # --------------------------------------------------------

    @classmethod
    def get_total_accounts(cls) -> int:
        """Return total number of bank accounts."""
        return BankAccount.total_accounts

    # --------------------------------------------------------
    # Dunder Methods
    # --------------------------------------------------------

    def __str__(self) -> str:
        """Return a user-friendly account representation."""
        return (
            f"{self.account_number} - "
            f"{self.__class__.__name__} - "
            f"₹{self._balance:,.2f}"
        )

    def __repr__(self) -> str:
        """Return a developer-friendly account representation."""
        return (
            f"{self.__class__.__name__}("
            f"account_number={self.account_number!r}, "
            f"customer_id={self.customer.customer_id!r}, "
            f"balance={self._balance!r})"
        )

    def __eq__(self, other: object) -> bool:
        """Compare accounts using account number."""
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self.account_number == other.account_number


# ============================================================
# Saving Account
# ============================================================


class SavingAccount(BankAccount):
    """Represent a savings account."""

    MINIMUM_BALANCE = 1000.0

    def withdraw(self, amount: float) -> None:
        """Withdraw money from a savings account."""
        self._validate_amount(amount)

        if self._balance - amount < self.MINIMUM_BALANCE:
            raise MinimumBalanceError(
                f"Savings account must maintain a minimum "
                f"balance of ₹{self.MINIMUM_BALANCE:.2f}."
            )

        self._balance -= amount

        self._add_transaction(
            transaction_type="WITHDRAWAL",
            amount=amount,
        )


# ============================================================
# Current Account
# ============================================================


class CurrentAccount(BankAccount):
    """Represent a current account."""

    OVERDRAFT_LIMIT = 5000.0

    def withdraw(self, amount: float) -> None:
        """Withdraw money from a current account."""
        self._validate_amount(amount)

        if self._balance - amount < -self.OVERDRAFT_LIMIT:
            raise InsufficientBalanceError(
                "Withdrawal exceeds the overdraft limit."
            )

        self._balance -= amount

        self._add_transaction(
            transaction_type="WITHDRAWAL",
            amount=amount,
        )


# ============================================================
# Bank
# ============================================================


class Bank:
    """Represent a bank."""

    def __init__(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Bank name cannot be empty.")

        self.name = name.strip()
        self._customers: dict[int, Customer] = {}
        self._accounts: dict[str, BankAccount] = {}

    # --------------------------------------------------------
    # Customer Management
    # --------------------------------------------------------

    def add_customer(self, customer: Customer) -> None:
        """Add a customer to the bank."""
        if customer.customer_id in self._customers:
            raise InvalidCustomerError("Customer ID already exists.")

        self._customers[customer.customer_id] = customer

    def get_customer(self, customer_id: int) -> Customer:
        """Return a customer by ID."""
        try:
            return self._customers[customer_id]
        except KeyError as error:
            raise CustomerNotFoundError(
                f"Customer {customer_id} not found.") from error

    # --------------------------------------------------------
    # Account Management
    # --------------------------------------------------------

    def add_account(self, account: BankAccount) -> None:
        """Add an account to the bank."""
        if account.account_number in self._accounts:
            raise AccountNotFoundError("Account number already exists.")

        self._accounts[account.account_number] = account
        account.customer.add_account(account)

    def get_account(self, account_number: str) -> BankAccount:
        """Return an account by account number."""
        try:
            return self._accounts[account_number]
        except KeyError as error:
            raise AccountNotFoundError(
                f"Account {account_number} not found."
                ) from error

    # --------------------------------------------------------
    # Banking Operations
    # --------------------------------------------------------

    def deposit(
        self,
        account_number: str,
        amount: float,
    ) -> None:
        """Deposit money into an account."""
        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw(
        self,
        account_number: str,
        amount: float,
    ) -> None:
        """Withdraw money from an account."""
        account = self.get_account(account_number)
        account.withdraw(amount)

    def transfer(
        self,
        source_account: str,
        target_account: str,
        amount: float,
    ) -> None:
        """Transfer money between accounts."""
        source = self.get_account(source_account)
        target = self.get_account(target_account)

        source.transfer(amount, target)

    def check_balance(self, account_number: str) -> float:
        """Check account balance."""
        account = self.get_account(account_number)
        return account.check_balance()

    def show_transaction_history(
        self,
        account_number: str,
    ) -> None:
        """Display transaction history."""
        account = self.get_account(account_number)

        print(f"\nTransaction History: {account_number}")
        print("-" * 60)

        for transaction in account.get_transaction_history():
            print(transaction)

    # --------------------------------------------------------
    # Dunder Methods
    # --------------------------------------------------------

    def __str__(self) -> str:
        """Return a user-friendly bank representation."""
        return (
            f"{self.name} | "
            f"Customers: {len(self._customers)} | "
            f"Accounts: {len(self._accounts)}"
        )

    def __repr__(self) -> str:
        """Return a developer-friendly bank representation."""
        return (
            f"Bank("
            f"name={self.name!r}, "
            f"customers={len(self._customers)}, "
            f"accounts={len(self._accounts)})"
        )


# ============================================================
# Main
# ============================================================


def main() -> None:
    """Run the banking management system."""

    try:
        bank = Bank(name="ABC Bank")

        customer1 = Customer(
            customer_id=101,
            name="Pradip",
            email="pradip@example.com",
            phone="9876543210",
        )

        customer2 = Customer(
            customer_id=102,
            name="Rahul",
            email="rahul@example.com",
            phone="9123456780",
        )

        bank.add_customer(customer1)
        bank.add_customer(customer2)

        saving_account = SavingAccount(
            account_number="SB1001",
            customer=customer1,
            initial_balance=10000,
        )

        current_account = CurrentAccount(
            account_number="CA1001",
            customer=customer2,
            initial_balance=5000,
        )

        bank.add_account(saving_account)
        bank.add_account(current_account)

        # ----------------------------------------------------
        # Display objects
        # ----------------------------------------------------

        print(bank)
        print(repr(bank))

        print("\nCustomers:")
        print(customer1)
        print(repr(customer1))

        print("\nAccounts:")
        print(saving_account)
        print(repr(saving_account))

        # ----------------------------------------------------
        # Deposit
        # ----------------------------------------------------

        bank.deposit(
            account_number="SB1001",
            amount=5000,
        )

        # ----------------------------------------------------
        # Withdrawal
        # ----------------------------------------------------

        bank.withdraw(
            account_number="SB1001",
            amount=2000,
        )

        # ----------------------------------------------------
        # Transfer
        # ----------------------------------------------------

        bank.transfer(
            source_account="SB1001",
            target_account="CA1001",
            amount=3000,
        )

        # ----------------------------------------------------
        # Balance Checking
        # ----------------------------------------------------

        print(
            f"\nSaving Account Balance: "
            f"₹{bank.check_balance('SB1001'):,.2f}"
        )

        print(
            f"Current Account Balance: "
            f"₹{bank.check_balance('CA1001'):,.2f}"
        )

        # ----------------------------------------------------
        # Transaction History
        # ----------------------------------------------------

        bank.show_transaction_history("SB1001")
        bank.show_transaction_history("CA1001")

        # ----------------------------------------------------
        # Equality
        # ----------------------------------------------------

        another_customer = Customer(
            customer_id=101,
            name="Another Name",
            email="another@example.com",
            phone="9000000000",
        )

        print(
            "\nCustomer equality:",
            customer1 == another_customer,
        )

        # ----------------------------------------------------
        # Class Methods
        # ----------------------------------------------------

        print(
            "\nTotal Customers:",
            Customer.get_total_customers(),
        )

        print(
            "Total Accounts:",
            BankAccount.get_total_accounts(),
        )

    except BankingError as error:
        print(f"Banking Error: {error}")

    except (TypeError, ValueError) as error:
        print(f"Input Error: {error}")


if __name__ == "__main__":
    main()
