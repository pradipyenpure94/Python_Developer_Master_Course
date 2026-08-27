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
    for num in range(0, number + 1,  2):
        sum_of_even_numbers += num

    print(f"Sum of even numbers from 1 to {number}: {sum_of_even_numbers}")
