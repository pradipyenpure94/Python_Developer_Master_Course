"""Average of list elements."""

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.0, 5.0, True, "hello"]

filtered_numbers = [num
                    for num in data
                    if isinstance(num, (float, int))
                    and not isinstance(num, bool)]
if filtered_numbers:
    average = sum(filtered_numbers) / len(filtered_numbers)
    print(f"Average: {average:.2f}")
else:
    print("No numeric values found.")
