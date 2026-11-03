"""Accept product name, quantity and price."""

name = input("Enter the product name: ")
quantity = int(input("Enter the product quantity: "))
price = float(input("Enter the product price: "))

total_price = price * quantity

print("-" * 25)
print("Product Information: ")
print("-" * 25)
print(f"Name         : {name}")
print(f"Quantity     : {quantity}")
print(f"Price        : {price:.2f}")
print("-" * 25)
print(f"Total price  : {total_price:.2f}")
