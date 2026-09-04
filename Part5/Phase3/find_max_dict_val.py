"""Find maximum dictionary value."""

my_dictionary = {"Pradip": 33, "Amit": 30}

max_dictionary = max(my_dictionary, key=my_dictionary.get)
print(f"MAximum dictionary: {max_dictionary}")
