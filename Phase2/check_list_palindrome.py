"""Check if list is palindrome."""

numbers = [1, 2, 3, 1]

if list(reversed(numbers)) == numbers:
    print("List is a palindrome.")
else:
    print("List is not a palindrome.")
