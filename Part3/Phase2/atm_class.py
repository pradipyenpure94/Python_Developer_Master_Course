"""
ATM PIN

Create an ATM class with a private PIN.

Implement:

    - PIN validation
    - withdrawal
    - balance checking
"""

from getpass import getpass

ATM_PIN_LENGTH = 4
MIN_BALANCE = 1000
WITHDRAWAL_MULTIPLE = 100


class ATM:
    """Represent an ATM."""

    def __init__(self, pin: str, initial_balance: float = 5000) -> None:
        self.validate_pin_format(pin=pin)
        if initial_balance < MIN_BALANCE:
            raise ValueError(
                "Initial balance must be greater than or equal to "
                f"{MIN_BALANCE}"
            )
        self.__pin = pin
        self.__balance = initial_balance

    def get_balance(self) -> float:
        """Return the ATM account balance."""
        return self.__balance

    def validate_pin_format(self, pin: str) -> None:
        """Validate ATM PIN format."""
        if len(pin) != ATM_PIN_LENGTH or not pin.isdigit():
            raise ValueError(
                f"ATM PIN must contain exactly {ATM_PIN_LENGTH} "
                "digits."
            )

    def verify_pin(self, pin: str) -> None:
        """Validate and verify the ATM PIN."""
        self.validate_pin_format(pin=pin)
        if self.__pin != pin:
            raise ValueError("Wrong PIN.")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the ATM account."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if amount % WITHDRAWAL_MULTIPLE != 0:
            raise ValueError(
                f"Amount should be a multiple of {WITHDRAWAL_MULTIPLE}."
            )
        if self.__balance - amount < MIN_BALANCE:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount


def main() -> None:
    """Run the main program."""

    try:
        atm_object = ATM(pin="1236")
        atm_pin = getpass("Enter the ATM PIN: ").strip()
        atm_object.verify_pin(pin=atm_pin)
        initial_balance = atm_object.get_balance()
        amount = float(input("Enter the withdrawal amount: "))
        atm_object.withdraw(amount=amount)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Current Balance       : {initial_balance:.2f}")
        print(f"Withdraw Amount       : {amount:.2f}")
        print(f"Final Balance         : {atm_object.get_balance():.2f}")


if __name__ == "__main__":
    main()
