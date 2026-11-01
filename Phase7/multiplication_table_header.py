"""Print a simple multiplication table header."""

number = 5

print("Multiplication Table")
print("-" * 10)
print("Number\tMultiplier\tResult")
print("-" * 10)
for i in range(1, 11):
    print(f"{number} \tx \t{i} \t= {number * i}")
