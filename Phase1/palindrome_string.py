"""Check whether a string is palindrome"""

text = input("Enter a string: ").strip().casefold()

reversed_string = "".join(reversed(text))

if text == reversed_string:
    print(f"{text} is a palindrome string.")
else:
    print(f"{text} is not a palindrome string.")
