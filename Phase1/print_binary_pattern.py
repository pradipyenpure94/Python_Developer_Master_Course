"""Print a right triangle binary pattern"""

for i in range(5):
    for j in range(i + 1):
        print((i + j + 1) % 2, end=" ")
    print()
