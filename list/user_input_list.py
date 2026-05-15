"""User input list."""

numbers = []

try:
    n = int(input("How many elements? "))
    if n <= 0:
        print("Please enter a positive integer for number of elements.")
    else:
        for _ in range(n):
            value = int(input("Enter a number: "))
            numbers.append(value)

        print(f"Numbers: {numbers}")

except ValueError:
    print("Invalid input! Please enter a positive integer.")
