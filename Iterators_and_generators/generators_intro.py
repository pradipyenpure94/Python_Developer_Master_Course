"""Generator vs List."""


numbers = [number for number in range(1, 5)]
print(numbers)

numbers = (number for number in range(1, 5))

print(next(numbers))
print(next(numbers))
print(next(numbers))
