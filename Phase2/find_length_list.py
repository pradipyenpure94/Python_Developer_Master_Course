"""Find length of list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length_of_list = 0
index = 0

while index < len(numbers):
    length_of_list += 1
    index += 1

print(f"Length of List: {length_of_list}")
