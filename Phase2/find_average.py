"""Find average of list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if numbers:
    length_of_list = len(numbers)
    sum_of_list = sum(numbers)

    average_of_numbers = sum_of_list / length_of_list
    print(f"Average of numbers: {average_of_numbers}")
else:
    print("List is empty!")
