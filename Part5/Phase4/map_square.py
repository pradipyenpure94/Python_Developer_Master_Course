"""Use map() to square list elements."""

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squares}")
