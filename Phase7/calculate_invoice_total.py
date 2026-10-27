"""Calculate an invoice total and format it to two decimal places."""


def calculate_tax_amount(amount: float, tax_rate: float) -> float:
    return amount * tax_rate / 100


def calculate_invoice_amount(amount: float, tax_amount: float) -> float:
    return amount + tax_amount


if __name__ == "__main__":
    try:
        amount = float(input("Enter the invoice amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        tax_rate = float(input("Enter the tax rate (%): "))
        if not 0 <= tax_rate <= 100:
            raise ValueError("Tax rate must be between 0 and 100.")

        tax_amount = calculate_tax_amount(amount=amount, tax_rate=tax_rate)
        invoice_amount = calculate_invoice_amount(
            amount=amount,
            tax_amount=tax_amount
        )
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Amount         : {amount:.2f}")
        print(f"Tax rate (%)   : {tax_rate:.2f}")
        print(f"Tax Amount     : {tax_amount:.2f}")
        print(f"Invoice Amount : {invoice_amount:.2f}")
