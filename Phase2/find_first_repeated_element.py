"""Find first repeated element."""

numbers = [1, 2, 3, 1, 5, 9, 2, 4, 7]

seen = set()
found = False
index = 0

while index < len(numbers):
    number = numbers[index]

    if number in seen:
        print(f"First repeated number: {number}")
        found = True
        break

    seen.add(number)

    index += 1

if not found:
    print("No repeated element found.")
