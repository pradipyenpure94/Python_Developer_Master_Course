"""Print multiplication tables from 1 to 10."""

index = 1
while index <= 10:
    j = 1
    table = f"Table of {index}"
    print(table.center(40, "-"))

    while j <= 10:
        print(f"{j} x {index} = {j * index}")
        j += 1
    index += 1
    print("-" * 40)
