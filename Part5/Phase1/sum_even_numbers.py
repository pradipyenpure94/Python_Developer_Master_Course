"""Find the sum of even numbers from 1 to N."""


try:
    number = int(input("Enter the number: "))
    if number < 0:
        raise ValueError("Number cannot be negative.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    sum_of_even_numbers = 0
    index = 0
    while index <= number:
        sum_of_even_numbers += index
        index += 2

    print(f"Sum of even numbers from 1 to {number}: {sum_of_even_numbers}")
