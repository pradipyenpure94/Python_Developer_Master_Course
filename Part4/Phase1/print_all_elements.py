"""Program 2: Print All Elements Using next()."""

numbers = (10, 20, 30, 40, 50)

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
