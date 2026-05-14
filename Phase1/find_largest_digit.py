"""Find the largest digit in a number."""

try:
    number = int(input("Enter a number: "))

    temp = abs(number)
    largest_digit = 0

    while temp > 0:
        digit = temp % 10
        if digit > largest_digit:
            largest_digit = digit
        temp //= 10

    print(f"Largest digit: {largest_digit}")

except ValueError:
    print("Invalid input! Please enter an integer.")
