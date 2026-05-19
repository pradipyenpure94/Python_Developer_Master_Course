"""Count even and odd numbers from list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

count_even_numbers = sum(1 for number in numbers
                         if isinstance(number, int) and number % 2 == 0)
count_odd_numbers = sum(1 for number in numbers
                        if isinstance(number, int) and number % 2 == 1)

print(f"Count even numbers: {count_even_numbers}")
print(f"Count odd numbers: {count_odd_numbers}")
