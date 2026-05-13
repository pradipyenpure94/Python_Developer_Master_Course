"""Frequency of character"""

text = input("Enter a sentence: ")
char = input("Enter a character: ")

count = 0

for ch in text:
    if char == ch:
        count += 1

print(f"Frequency: {count}")
