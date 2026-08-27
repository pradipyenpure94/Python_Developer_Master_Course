"""Count numbers divisible by 3 between 1 and N."""


count = 0

try:
    number = int(input("Enter the number: "))
    if number <= 0:
        raise ValueError("Number must be greater than zero.")
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    count = len(range(3, number + 1, 3))
    print(f"Count numbers from 1 to {number}: {count}")
