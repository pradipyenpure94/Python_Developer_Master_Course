"""Sort dictionary by values."""

my_dictionary = {"apple": 30, "cherry": 25, "banana": 29}

result = dict(sorted(my_dictionary.items(), key=lambda x: x[1]))
print(f"Sorted dictionary by values: {result}")
