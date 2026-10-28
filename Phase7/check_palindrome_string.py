"""Check whether a string is a palindrome, ignoring case."""

text = "Madam1"
reverse_string = text[::-1]

if text.casefold() == reverse_string.casefold():
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")
