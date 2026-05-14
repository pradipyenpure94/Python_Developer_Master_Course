"""Right triangle continuous increasing number pattern."""

number = 1
for i in range(1, 5):
    for _ in range(i):
        print(number, end=" ")
        number += 1
    print()
