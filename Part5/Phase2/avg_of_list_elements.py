"""Find average of list elements."""


numbers = [1, 2, 3, 4, 5]

count_elements = 0
total_of_elements = 0

for number in numbers:
    count_elements += 1
    total_of_elements += number

average = total_of_elements / count_elements
print(f"Average: {average:.2f}")
