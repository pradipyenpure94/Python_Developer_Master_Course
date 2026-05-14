"""Arithmetic calculator"""

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice? ")

if choice not in {"1", "2", "3", "4"}:
    print("Invalid choice! Please enter a valid choice (1-4).")
else:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        match choice:
            case "1":
                print(f"Addition: {num1 + num2}")
            case "2":
                print(f"Subtraction: {num1 - num2}")
            case "3":
                print(f"Multiplication: {num1 * num2}")
            case "4":
                try:
                    print(f"Division: {num1 / num2}")
                except ZeroDivisionError as error:
                    print(error)

    except ValueError:
        print("Invalid input! Please enter a number.")
