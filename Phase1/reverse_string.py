"""Reverse a string"""

text = input("Enter a text: ")

reversed_string = ""

for index in range(len(text) - 1, -1, -1):
    reversed_string += text[index]

print(f"Reversed string: {reversed_string}")
