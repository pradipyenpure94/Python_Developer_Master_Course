"""Reverse a string using slicing and then using a loop."""

text = "Pradip"
reversed_text = text[::-1]
# print(f"Reverse text: {reversed_text}")

reversed_string = ""

for char in text:
    reversed_string = char + reversed_string

print(reversed_string)
