"""Create an abstract Payment class."""

from abc import ABC, abstractmethod


class Payment(ABC):
    """Represent an abstract payment."""

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process the payment."""
        pass


class GooglePay(Payment):
    """Represent a Googlepay payment."""

    def pay(self, amount: float) -> None:
        print(f"{amount:.2f} pay using google pay.")


class Phonepe(Payment):
    """Represent a phonepe payment."""

    def pay(self, amount: float) -> None:
        print(f"{amount:.2f} pay using phonepe.")


def main() -> None:
    """Run the main program."""

    payments = [GooglePay(), Phonepe()]

    amount = 5000
    for payment in payments:
        payment.pay(amount=amount)


if __name__ == "__main__":
    main()
