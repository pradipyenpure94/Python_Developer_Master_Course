"""Find the sum of odd numbers from 1 to N."""

try:
    number = int(input("Enter the number: "))
    if number < 0:
        raise ValueError("Number cannot be negative.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    sum_odd_numbers = sum(range(1, number + 1, 2))

    print(f"Sum of Odd numbers from 1 to {number}: {sum_odd_numbers}")
