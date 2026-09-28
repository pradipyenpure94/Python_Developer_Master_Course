"""Validate transaction amount."""


def validate_amount(func):
    """Create validate transaction amount decorator."""
    def wrapper(amount: float):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return func(amount)
    return wrapper


@validate_amount
def deposit_amount(amount: float):
    """Transaction Entry."""
    print(f"Deposited amount: {amount:.2f}")


if __name__ == "__main__":
    try:
        deposit_amount(amount=0.1)
    except ValueError as error:
        print(f"Error: {error}")
