"""Count even and odd numbers from list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

count_even_numbers = 0
count_odd_numbers = 0
index = 0

while index < len(numbers):
    current_number = numbers[index]

    if isinstance(current_number, int):
        if current_number % 2 == 0:
            count_even_numbers += 1
        else:
            count_odd_numbers += 1
    index += 1

print(f"Count even numbers: {count_even_numbers}")
print(f"Count odd numbers: {count_odd_numbers}")
