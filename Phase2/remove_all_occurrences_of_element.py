"""Remove all occurrences of element."""

numbers = [1, 2, 3, 2, 5, 6, 4, 2, 0, 8, 5, 0, 7, 9]
target = 2

print(f"Numbers: {numbers}")
filtered_numbers = [number for number in numbers if number != target]
print(f"Remove {target} from list: {filtered_numbers}")
