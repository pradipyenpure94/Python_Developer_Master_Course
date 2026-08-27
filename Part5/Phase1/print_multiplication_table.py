"""Print multiplication table of a number."""


try:
    number = int(input("Enter the number: "))
    if number <= 0:
        raise ValueError("Number must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
