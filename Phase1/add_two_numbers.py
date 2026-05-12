"""sum of two numbers"""

try:
    num1 = int(value) if (value:= input("Enter first number: ")).isdigit() else float(value)
    num2 = int(value) if (value:= input("Enter second number: ")).isdigit() else float(value)
    print(f"Sum: {num1 + num2}")
except ValueError:
    print("Invalid input! Please enter a number.")
