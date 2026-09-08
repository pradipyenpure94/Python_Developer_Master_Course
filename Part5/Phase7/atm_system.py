"""Build robust ATM system with exception handling."""


class InsufficientAccountBalance(Exception):
    """Insufficient account balance."""


ACCOUNT_BALANCE = 1000


def check_account_balance() -> None:
    """Check the account balance."""
    print(f"Current Balance: {ACCOUNT_BALANCE:.2f}")


def deposit_money(amount: float) -> None:
    """Deposit amount to the account."""
    global ACCOUNT_BALANCE
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")

    ACCOUNT_BALANCE += amount


def withdraw(amount: float) -> None:
    """Withdraw amount from ATM account."""
    global ACCOUNT_BALANCE
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")
    if amount > ACCOUNT_BALANCE:
        raise InsufficientAccountBalance("Insufficient account balance.")
    ACCOUNT_BALANCE -= amount


def main() -> None:
    """Run the main program."""
    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice not in {"1", "2", "3", "4"}:
                print("Please select a valid option (1-4).")
                continue

            if choice == "4":
                print("Exit from operations.")
                break

            if choice == "1":
                check_account_balance()

            if choice == "2":
                amount = float(input("Enter the amount: "))
                deposit_money(amount=amount)

            if choice == "3":
                amount = float(input("Enter the amount: "))
                withdraw(amount=amount)

        except (ValueError, InsufficientAccountBalance) as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
            break


if __name__ == "__main__":
    main()
