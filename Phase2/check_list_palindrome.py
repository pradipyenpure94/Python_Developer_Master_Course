"""Check if list is palindrome."""

numbers = [1, 2, 1, 1]

left = 0
right = len(numbers) - 1

is_palindrome = True

while left < right:
    if numbers[left] != numbers[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print(f"{numbers} is palindrome.")
else:
    print(f"{numbers} is not palindrome.")
