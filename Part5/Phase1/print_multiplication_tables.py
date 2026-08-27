"""Print multiplication tables from 1 to 10."""

for number in range(1, 11):
    table = f"Table of {number}"
    print(table.center(40, "-"))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    print("-" * 40)
