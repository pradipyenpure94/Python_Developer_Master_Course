"""Remove all occurrences of element."""

numbers = [1, 2, 3, 2, 5, 6, 4, 2, 0, 8, 5, 0, 7, 9]
target = 2

print(f"Numbers: {numbers}")
filtered_numbers = list(filter(lambda number:  number != target, numbers))
print(f"Remove {target} from list: {filtered_numbers}")
