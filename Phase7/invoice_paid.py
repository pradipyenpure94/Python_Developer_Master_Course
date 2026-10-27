"""Classify an invoice as unpaid, partially paid or paid."""


def calculate_paid_amount_percentage(
    invoice_amount: float,
    paid_amount: float
) -> float:
    return (paid_amount / invoice_amount) * 100


def check_paid_status(
    invoice_amount: float,
    paid_amount: float
) -> tuple[str, float]:
    paid_amount_percentage = calculate_paid_amount_percentage(
        invoice_amount=invoice_amount,
        paid_amount=paid_amount
    )

    if paid_amount_percentage <= 0:
        return "Unpaid", paid_amount_percentage
    elif paid_amount_percentage < 100:
        return "Partially Paid", paid_amount_percentage
    else:
        return "Paid", paid_amount_percentage


if __name__ == "__main__":
    try:
        invoice_amount = float(input("Enter the amount: "))
        if invoice_amount <= 0:
            raise ValueError("Invoice amount must be greater than zero.")

        paid_amount = float(input("Enter the paid amount: "))
        if paid_amount > invoice_amount:
            raise ValueError(
                "Payment cannot exceed the invoice amount of "
                f"{invoice_amount:.2f}."
            )
        if paid_amount < 0:
            raise ValueError("Paid amount cannot be negative.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        paid_status, paid_amount_percentage = check_paid_status(
            invoice_amount=invoice_amount,
            paid_amount=paid_amount
        )
        print(f"Invoice amount   : {invoice_amount:.2f}")
        print(f"Paid amount      : {paid_amount:.2f}")
        print(f"Paid percentage  : {paid_amount_percentage:.2f}%")
        print(f"Status           : {paid_status}")
