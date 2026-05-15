"""User input list."""

numbers = []

try:
    n = int(input("How many elements? "))
    if n <= 0:
        print("Please enter a positive integer for number of elements.")
    else:
        index = n - 1
        while index >= 0:
            try:
                value = int(input("Enter a number: "))
                numbers.append(value)
                index -= 1
            except ValueError:
                print("Invalid input! Please enter an integer.")
                continue

        print(f"Numbers: {numbers}")

except ValueError:
    print("Invalid input! Please enter a positive integer.")
