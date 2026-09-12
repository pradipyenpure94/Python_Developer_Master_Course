"""Iterate over list using next() and iter() and while loop."""

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("Error: StopIteration")
        break
