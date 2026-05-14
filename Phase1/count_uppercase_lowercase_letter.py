"""Count uppercase and lowercase letters in a string."""

text = input("Enter a string: ")

lower = 0
upper = 0

for char in text.strip():
    if char.islower():
        lower += 1
    elif char.isupper():
        upper += 1

print(f"Lowercase letters: {lower}\nUppercase letters: {upper}")
