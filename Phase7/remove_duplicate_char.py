"""Remove duplicate characters while preserving order."""

text = "Pradip".casefold()

remove_duplicate_chars = "".join(dict.fromkeys(text))
print(remove_duplicate_chars)
