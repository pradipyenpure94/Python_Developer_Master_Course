"""Count vowels, consonants, digits and spaces."""

vowels = "aeiou"

text = "Pra di p56@ # $".casefold()

vowels_count = 0
consonant_count = 0
digits_count = 0
spaces_count = 0

for char in text:
    if char in vowels:
        vowels_count += 1
    if char.isalpha() and char not in vowels:
        consonant_count += 1
    if char.isdigit():
        digits_count += 1
    if char.isspace():
        spaces_count += 1

print(f"Vowels count     : {vowels_count}")
print(f"Consonants count : {consonant_count}")
print(f"Digits count     : {digits_count}")
print(f"Spaces count     : {spaces_count}")
