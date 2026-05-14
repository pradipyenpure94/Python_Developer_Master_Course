"""Count each character frequency."""

text = input("Enter a string: ")

for char in text.strip():
    print(f"{char}: {text.count(char)}")
