"""Print continuous increasing alphabet pattern."""

number = 65
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(number), end=" ")
        number += 1
    print()
