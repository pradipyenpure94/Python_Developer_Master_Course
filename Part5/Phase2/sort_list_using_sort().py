"""Sort a list using sort()."""


alphabets = ["A", "a", "b", "c", "B", "F", "D", "d"]

alphabets.sort(key=str.lower, reverse=True)
print(f"Sorted Alphabets: {alphabets}")
