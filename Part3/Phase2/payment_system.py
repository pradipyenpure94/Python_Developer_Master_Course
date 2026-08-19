"""
Payment System

Create:

    Payment
    ├── CreditCardPayment
    ├── UPIPayment
    └── CashPayment

Each class should implement:

    make_payment()

Demonstrate polymorphism.
"""


class Payment:
    """Represent a payment."""

    def make_payment(self) -> None:
        """Make the payment."""
        raise NotImplementedError


class CreditCardPayment(Payment):
    """Represent a credit card payment."""

    def make_payment(self) -> None:
        """Make a credit card payment."""
        print("Credit card payment.")


class UPIPayment(Payment):
    """Represent a UPI Payment."""

    def make_payment(self) -> None:
        """Make a UPI Payment."""
        print("UPI Payment.")


class CashPayment(Payment):
    """Represent a cash payment."""

    def make_payment(self) -> None:
        """Make a cash payment."""
        print("Cash Payment")


def main() -> None:
    """Run the main program."""
    payments = [CreditCardPayment(), UPIPayment(), CashPayment()]

    for payment in payments:
        payment.make_payment()


if __name__ == "__main__":
    main()
