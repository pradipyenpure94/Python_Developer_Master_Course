"""Log Finacial Transaction."""


def log(func):
    """Finacial transaction log."""
    def wrapper(*args, **kwargs):
        print("Transaction started.")
        result = func(*args, **kwargs)
        print("Transaction completed.")
        return result
    return wrapper


@log
def deposit(amount: float):
    print(f"Deposited amount: {amount:.2f}")


if __name__ == "__main__":
    deposit(amount=250)
