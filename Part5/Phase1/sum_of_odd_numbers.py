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
    sum_odd_numbers = 0
    for num in range(1, number + 1, 2):
        sum_odd_numbers += num

    print(f"Sum of Odd numbers from 1 to {number}: {sum_odd_numbers}")
