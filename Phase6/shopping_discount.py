"""Shopping discount."""

price = float(input("Enter the product price: "))
quantity = float(input("Enter the product quantity: "))

# Discount %
discount = 10

total_price = price * quantity
subtotal = total_price * 10 / 100
final_total = total_price - subtotal
print(f"Product price with discount: {final_total:.2f}")
