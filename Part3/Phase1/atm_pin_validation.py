"""ATM PIN validation."""

ATM_PIN_LENGTH = 4


def validate_atm_pin(atm_pin: str) -> None:
    """Validate the ATM PIN."""
    if len(atm_pin) != ATM_PIN_LENGTH:
        raise ValueError(
            f"ATM PIN length should be {ATM_PIN_LENGTH} digits."
        )
    if not atm_pin.isdigit():
        raise ValueError("The ATM PIN should be in digits.")


class ATM:
    """Represent an ATM."""
    def __init__(self, atm_pin: str) -> None:
        validate_atm_pin(atm_pin=atm_pin)
        self.__atm_pin = atm_pin

    def get_atm_pin(self) -> str:
        """Return the ATM PIN."""
        return self.__atm_pin


def main() -> None:
    """Run the main program."""
    try:
        atm_pin = input("Enter the ATM PIN: ")
        atm_obj = ATM(atm_pin=atm_pin)
        print(f"ATM PIN: {atm_obj.get_atm_pin()}")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


if __name__ == "__main__":
    main()
