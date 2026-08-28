"""Find the product of digits of a number."""


try:
    number = int(input("Enter the number: "))

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    number = abs(number)
    product_of_digits = 1
    if number == 0:
        product_of_digits = 0

    while number > 0:
        digit = number % 10
        product_of_digits *= digit
        number //= 10

    print(f"Product of digits: {product_of_digits}")
