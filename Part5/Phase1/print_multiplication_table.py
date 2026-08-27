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
    index = 1

    while index <= 10:
        print(f"{number} x {index} = {number * index}")
        index += 1
