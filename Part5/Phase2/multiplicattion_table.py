"""create a multiplication table using list comprehsnion."""

number = 2

multiplication_table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
print(multiplication_table)
