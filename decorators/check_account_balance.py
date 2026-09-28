"""Check account balance."""

balance = 500


def sufficient_balance(func):
    """Sufficient balance decorator."""
    def wrapper(amount: float):
        if balance < amount:
            raise ValueError("Insufficient balance.")
        return func(amount)
    return wrapper


@sufficient_balance
def withdraw(amount: float):
    print(f"Withdraw amount: {amount:.2f}")


if __name__ == "__main__":
    try:
        withdraw(amount=200)
    except ValueError as e:
        print(f"Error: {e}")
