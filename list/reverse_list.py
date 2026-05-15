"""Reverse List"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = len(numbers) - 1
reversed_list = []

while index >= 0:
    reversed_list.append(numbers[index])
    index -= 1

print(f"Reversed List: {reversed_list}")
