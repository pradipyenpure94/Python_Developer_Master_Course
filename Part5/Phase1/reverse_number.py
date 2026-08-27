"""Reverse a number."""


try:
    number = int(input("Enter the number: "))
    sign = -1 if number < 0 else 1

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    number = abs(number)
    reverse_number = 0
    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number //= 10
    print(f"Reverse Number: {reverse_number * sign}")
