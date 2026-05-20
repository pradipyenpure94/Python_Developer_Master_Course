"""Check if list is palindrome."""

numbers = [1, 2, 1]

if numbers[::-1] == numbers:
    print("List is a palindrome.")
else:
    print("List is not a palindrome.")
