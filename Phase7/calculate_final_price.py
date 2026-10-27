"""Calculate discount discount and final selling price."""

try:
    # Accept input from user.
    price = float(input("Enter the product price: "))
    if price <= 0:
        raise ValueError("Product price must be greater than zero.")

    discount = float(input("Enter the discount (%): "))
    if not 0 <= discount <= 100:
        raise ValueError("Product discount must be between (0-100).")
except ValueError as error:
    print(f"Error: {error}")
else:
    product_discount = price * discount / 100
    final_price = price - product_discount
    print(f"Discount    : {product_discount:.2f}")
    print(f"Final price : {final_price:.2f}")
