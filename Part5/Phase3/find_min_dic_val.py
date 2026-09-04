"""Find minimum dictionary key value."""

my_dictionary = {"Pradip": 33, "Amit": 30}

min_key = min(my_dictionary, key=my_dictionary.get)
print(f"Min. Key: {min_key}, Value: {my_dictionary[min_key]}")
