"""Find first repeated element."""

numbers = [1, 2, 3, 1, 5, 9, 2, 4, 7]

seen = set()
found = False

for number in numbers:
    if number in seen:
        print(f"First repeated number: {number}")
        found = True
        break
    seen.add(number)

if not found:
    print("No repeated element found.")
