"""Calculate a product's total price using quantity and unit price."""

try:
    # Accept product price and its quantity
    price = float(input("Enter the product price: "))
    if price <= 0:
        raise ValueError("Product price must be greater than zero.")

    quantity = int(input("Enter the product quantity: "))
    if quantity <= 0:
        raise ValueError("Product quantity must be greater than zero.")
except ValueError as error:
    print(f"Error: {error}")
else:
    total_price = price * quantity
    print(f"Total price: {total_price:.2f}")
