"""Remove all occurrences of element."""

numbers = [1, 2, 3, 2, 5, 6, 4, 2, 0, 8, 5, 0, 7, 9]
target = 2

filtered_numbers = []
index = 0

while index < len(numbers):
    current_number = numbers[index]
    if current_number != target:
        filtered_numbers.append(current_number)
    index += 1

print(f"Before removing numbers: {numbers}")
print(f"After removing {target} from list: {filtered_numbers}")
