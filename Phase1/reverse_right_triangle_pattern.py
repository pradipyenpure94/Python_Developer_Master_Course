"""Reverse right triangle number continuous increasing pattern"""

number = 1
for i in range(10, -1, -1):
    for _ in range(i+1):
        print(number, end=" ")
        number += 1
    print()
