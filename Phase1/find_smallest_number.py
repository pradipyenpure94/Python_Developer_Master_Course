"""Find the smallest number."""

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    if num1 <= num2 and num1 <= num3:
        print(f"{num1} is the smallest number.")
    elif num2 <= num3 and num2 <= num1:
        print(f"{num2} is the smallest number.")
    else:
        print(f"{num3} is the smallest number.")

except ValueError:
    print("Invalid input! Please enter a number.")
