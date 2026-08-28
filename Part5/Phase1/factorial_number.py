"""Find the factorial of a number."""

try:
    number = int(input("Enter the number: "))
    if number < 0:
        raise ValueError(
            "A factorial number is not defined for negative number."
        )

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    fact = 1
    if number == 0 or number == 1:
        fact = 1

    for num in range(2, number + 1):
        fact *= num

    print(f"The factorial of {number} is: {fact}")
