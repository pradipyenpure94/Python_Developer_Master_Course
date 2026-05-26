"""Check anagram strings."""

import string

text1 = "".join(char for char in "silent! ".casefold() 
                if char not in string.punctuation and not char.isspace())
text2 = "".join(char for char in "list    en   ".casefold()
                if char not in string.punctuation and not char.isspace())

is_anagram = sorted(text1) == sorted(text2)
print(f"Is anagram: {is_anagram}")
