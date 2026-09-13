"""Multiplication Table Generator."""


def generate_multiplication_table(number: int):
    """Generate the multiplication table."""
    for i in range(1, 11):
        yield f"{number} * {i} = {number * i}"


if __name__ == "__main__":
    table = generate_multiplication_table(number=5)
    print(next(table))
    print(next(table))
    print(next(table))
    print("In for loop")
    for num in table:
        print(num)
