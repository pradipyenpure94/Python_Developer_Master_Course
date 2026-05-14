"""Reverse words in string."""

text = input("Enter a string: ")

words = text.split()
reversed_string = " ".join(reversed(words))
print(f"Reversed string: {reversed_string}")
