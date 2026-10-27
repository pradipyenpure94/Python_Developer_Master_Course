"""Calculate GST and the final invoice amount."""

try:
    # Accept input from user.
    amount = float(input("Enter the amount: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    tax_rate = float(input("Enter the tax rate (%): "))
    if not 0 <= tax_rate <= 100:
        raise ValueError("GST tax rate must be between (0-100).")

except ValueError as error:
    print(f"Error: {error}")
else:
    tax_amount = amount * tax_rate / 100
    final_invoice_amount = amount + tax_amount
    print(f"Tax amount: {tax_amount:.2f}")
    print(f"Final invoice amount: {final_invoice_amount:.2f}")
