"""Abstraction."""


from abc import ABC, abstractmethod


class Payment(ABC):
    """Abstract base class."""

    def __init__(self, amount: float, payment_type: str) -> None:
        if amount <= 0:
            raise ValueError(
                f"{payment_type}: Amount must be greater than zero."
            )
        self.amount = amount
        self.payment_type = payment_type

    @abstractmethod
    def pay(self) -> None:
        """Every payment method must implement this method."""


class UPIPayment(Payment):
    """Represent a UPI Payment."""
    def __init__(self, amount: float) -> None:
        super().__init__(amount, "UPI Payment")

    def pay(self) -> None:
        print(f"{self.amount:.2f} paid using {self.payment_type}")


class WalletPayment(Payment):
    """Represent a Wallet Payment."""
    def __init__(self, amount: float) -> None:
        super().__init__(amount, "Wallet Payment")

    def pay(self) -> None:
        print(f"{self.amount:.2f} paid using {self.payment_type}.")


def main() -> None:
    """Run the Main Program."""

    try:
        payments = [
            UPIPayment(5000),
            WalletPayment(100)
        ]
        for payment in payments:
            payment.pay()
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
