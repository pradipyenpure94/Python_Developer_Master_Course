"""Inventory management system."""

inventory = {}

while True:
    print("1. Add item.")
    print("2. View items.")
    print("3. Exit.")

    choice = input("Enter your choice? ")

    if choice not in {"1", "2", "3"}:
        print("Invalid choice! Please enter valid choice(1-3).")
        continue

    if choice == "1":
        name = input("Enter an item name: ")

        if name in inventory:
            print(f"{name} already exists!")
            continue

        if not name:
            print("Name cannot be empty!")
            continue

        try:
            quantity = int(input(f"Enter a quantity for {name}: "))
            price = float(input(f"Enter a price for {name}: "))

            if quantity < 0 or price < 0:
                print("Quantity and price cannot be negative.")
                continue

            inventory[name] = {
                "quantity": quantity,
                "price": price}

            print("Item added successfully!")

        except ValueError:
            print("Invalid input.")
            continue

    elif choice == "2":
        print("Product details:")
        if not inventory:
            print("Item stock entry not found!")
        else:
            print("-"*70)
            print(f"{'Sr.No':<10} | {'Name':<20} | {'Quantity':<10} | {'Price':<20}")
            print("-"*70)
            for index, (name, details) in enumerate(inventory.items(), start=1):
                print(f"{index:<10} | {name:<20} | {details['quantity']:<10}"
                      f" |  {details['price']:<20.2f}")
                print("-"*70)

    elif choice == "3":
        print("Exit")
        break
