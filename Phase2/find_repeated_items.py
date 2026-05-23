"""Find repeated items in tuple."""

numbers = (1, 2, 3, 1, 5, 9, 2, 5, 8, 3, 4, 7, 2, 5, 9, 8, 5, 4, 2, 1)

freq = dict()
index = 0

while index < len(numbers):
    number = numbers[index]
    freq[number] = freq.get(number, 0) + 1
    index += 1

repeated_items = [num
                  for num, count in freq.items()
                  if count > 1]
print(f"Repeated items: {repeated_items}")
