"""Perform all set operations menu-driven."""

prime_numbers = {2, 3, 5, 7, 11, 13}
odd_numbers = {1, 3, 5, 7, 9, 11, 13}

while True:
    print("Set Operations menu: ")
    print("1. Union set ")
    print("2. Intersection set ")
    print("3. Difference set ")
    print("4. Symmetric difference set ")
    print("5. Is Subset? ")
    print("6. Is Superset? ")
    print("7. Exit ")

    choice = input("Enter your choice? ")

    if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
        print("Invalid choice! Please enter correct choice (1-7)")
    elif choice == "7":
        print("Exit")
        break
    elif choice == "1":
        # Union: Elements in either prime_numbers or odd_numbers
        result = prime_numbers.union(odd_numbers)
        print(f"Result: {result}")
    elif choice == "2":
        # Intersection: common element in both prime_numbers and odd_numbers
        result = prime_numbers.intersection(odd_numbers)
        print(f"Result: {result}")
    elif choice == "3":
        # Difference: Element in prime_numbers but not in odd_numbers
        result = prime_numbers.difference(odd_numbers)
        print(f"Result: {result}")
    elif choice == "4":
        # Symmetric difference: Elemente in prime_numbers or odd_numbers,
        # but not both
        result = prime_numbers.symmetric_difference(odd_numbers)
        print(f"Result: {result}")
    elif choice == "5":
        # Is subset, Return True, if all values of prime_numbers are in
        # odd_numbers
        result = prime_numbers.issubset(odd_numbers)
        print(f"Result: {result}")
    elif choice == "6":
        # Is superset, Return True, if all values of odd_numbers are in
        # prime_numbers
        result = prime_numbers.issuperset(odd_numbers)
        print(f"Result: {result}")
