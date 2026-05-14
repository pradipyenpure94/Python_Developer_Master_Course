"""Calculate the power of number."""


try:
    base = int(input("Enter base: "))
    power = int(input("Enter power: "))

    result = base ** power
    print(f"Power of number: {result}")

except ValueError:
    print("Invalid input! Please enter an integer.")
