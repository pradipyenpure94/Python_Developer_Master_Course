"""Reverse List"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

length = len(numbers)
reversed_list = []

for index in range(length - 1, -1, -1):
    reversed_list.append(numbers[index])

print(f"Reversed List: {reversed_list}")
