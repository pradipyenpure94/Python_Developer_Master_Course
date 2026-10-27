"""Validate whether a customer qualifies for a discount."""


def is_eligible_for_discount(amount: float) -> bool:
    return amount >= 1000


if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        if is_eligible_for_discount(amount=amount):
            print("Customer qualifies for a discount")
        else:
            print("Customer does not qualify for a discount.")
