"""Find the length of a list."""


numbers = [1, 2, 3, 4, 5]
count_length = 0
index = 0

while index < len(numbers):
    count_length += 1
    index += 1

print(f"Length of list: {count_length}")
