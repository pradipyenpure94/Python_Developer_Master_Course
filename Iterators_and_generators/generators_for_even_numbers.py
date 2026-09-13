"""Generators for even numbers."""


def even_numbers(limit):
    """print even numbers"""
    for number in range(2, limit + 1, 2):
        yield number


for number in even_numbers(10):
    print(number)
