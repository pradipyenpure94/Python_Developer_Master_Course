"""Frequency counter."""

numbers = [12, 34, 56, 78, 9, 12, 34, 56]

for num in set(numbers):
    print(f"{num} = {numbers.count(num)}")
