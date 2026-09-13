"""List comprehension Vs Generators."""

squres = [number ** 2 for number in range(1, 5)]
print(squres)   # List comprehension

def squres_numbers(limit: int) -> None:
    for number in range(1, limit + 1):
        yield number ** 2


for number in squres_numbers(5):
    print(number)
