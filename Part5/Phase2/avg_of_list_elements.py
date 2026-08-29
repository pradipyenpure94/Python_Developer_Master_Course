"""Find average of list elements."""


numbers = [1, 2, 3, 4, 5]

count_elements = len(numbers)
total_of_elements = 0
index = 0

while index < count_elements:
    total_of_elements += numbers[index]
    index += 1

average = total_of_elements / count_elements
print(f"Average: {average:.2f}")
