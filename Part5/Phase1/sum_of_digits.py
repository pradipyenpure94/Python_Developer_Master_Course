"""Find the sum of digits of a number."""

try:
    number = int(input("Enter the number: "))

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:

    sum_of_digits = 0
    number = abs(number)

    while number > 0:
        digit = number % 10
        sum_of_digits += digit
        number //= 10

    print(f"Sum of digits: {sum_of_digits}")
