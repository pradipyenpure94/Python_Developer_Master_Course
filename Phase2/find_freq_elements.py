"""Find frequency of each element."""

from collections import Counter

numbers = [1, 2, 3, 1, 4, 7, 2, 5, 8, 3, 6, 9, 9, 8, 7, 4, 5, 6, 7, 4, 4, 4]

freq = Counter(numbers)

for number, count in freq.items():
    print(f"Frequency of {number} is {count}")
