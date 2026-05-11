"""Arithmetic Operators / Simple calculator"""

HORIZONTAL_LINE = "*"*50

while True:
    print(" Operations Menu ".center(50, "*"))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus (Remainder)")
    print("7. Exponent (Power)")
    print("8. Exit")
    print(HORIZONTAL_LINE)

    choice = input("Enter your choice? ")

    if choice == "8":
        print("Exit..!")
        break

    elif choice not in {"1", "2", "3", "4", "5", "6", "7"}:
        print("Invalid choice! Please enter valid choice (1-8).")
        continue

    try:
        num1 = int(value) if (value:= input("Enter a first number: ")).isdigit() else float(value)
        num2 = int(value) if (value:= input("Enter a second number: ")).isdigit() else float(value)

        if choice in {"4", "5", "6"} and num2 == 0:
            print("Cannot divide by zero!")
            continue

        elif choice == "1":
            print(f"Addition: {num1 + num2}")

        elif choice == "2":
            print(f"Subtraction: {num1 - num2}")

        elif choice == "3":
            print(f"Multiplication: {num1 * num2}")

        elif choice == "4":
            print(f"Division: {num1 / num2:.2f}")

        elif choice == "5":
            print(f"Floor Division: {num1 // num2}")

        elif choice == "6":
            print(f"Modulus (Remainder): {num1 % num2}")

        elif choice == "7":
            print(f"Exponent (Power): {num1 ** num2}")

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
