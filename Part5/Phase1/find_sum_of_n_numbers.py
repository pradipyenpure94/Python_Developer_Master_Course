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
    for number in range(1, number_limit + 1):
        sum_of_numbers += number

    print(f"Sum of 1 to {number_limit}: {sum_of_numbers}")
