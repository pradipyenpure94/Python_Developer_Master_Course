"""Create different payment classed with pay()."""


class Payment:
    """Represent a payment."""

    def pay(self) -> None:
        print("Payment processing.")


class GooglePay(Payment):
    """Represent a gpay."""

    def pay(self) -> None:
        print("Payment using google pay.")


class PhonePe(Payment):
    """Represent a phone pay."""

    def pay(self) -> None:
        print("Payment using phone pay.")


def main() -> None:
    """Run the main program."""

    payments = [Payment(), GooglePay(), PhonePe()]

    for payment in payments:
        payment.pay()


if __name__ == "__main__":
    main()
