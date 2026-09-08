"""Handle invalid list index."""

numbers = [1, 2, 3, 4, 5]

try:
    result = numbers[4]
except IndexError as error:
    print(f"Error: {error}")
else:
    print(f"Result: {result}")
