"""Calculate a shopping bill using user input."""

total_shopping_bill = 0
items_details = []

while True:
    name = input("Enter the product name: ").strip()
    if name.casefold() == "done":
        break

    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the product quantity: "))
    total_price = price * quantity
    total_shopping_bill += total_price
    items_details.append(
        {
            "name": name,
            "price": f"{price:.2f}",
            "quantity": quantity,
            "total": f"{total_price}"
        }
    )

print("-" * 125)
print(f"{'Sr. No':<10} | {'Item':<25} | {'Price':>25} | {'Quantity':>25} | {'Total':>25}")
print("-" * 125)
for index, item in enumerate(items_details, start=1):
    print(f"{index:<10} | {item.get("name"):<25} | {item.get("price"):>25} | {item.get("quantity"):>25} | {item.get("total"):>25}")
print("-" * 125)
print(f"Total Bill: {total_shopping_bill}")
