"""Count digits of a number."""


try:
    number = int(input("Enter the number: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    number = abs(number)
    digits_count = 0
    if number == 0:
        digits_count = 1
    while number > 0:
        digit = number % 10
        digits_count += 1
        number //= 10
    print(f"Total digits count: {digits_count}")
