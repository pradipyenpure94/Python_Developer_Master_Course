"""Reverse right triangle number continuous increasing pattern"""

number = 1
for i in range(10, -1, -1):
    for j in range(1, i+1):
        print(j, end=" ")
        number += 1
    print()
