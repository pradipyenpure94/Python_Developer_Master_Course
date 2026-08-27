"""Find the sum of numbers from 1 to N."""

try:
    number_limit = int(input("Enter the number: "))
    if number_limit <= 0:
        raise ValueError("Number limit must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    sum_of_numbers = 0
    index = 1

    while index <= number_limit:
        sum_of_numbers += index
        index += 1

    print(f"Sum of 1 to {number_limit}: {sum_of_numbers}")
