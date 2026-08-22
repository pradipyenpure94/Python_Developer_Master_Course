"""Introduction to Iterators."""

# Example: 1
# List:

numbers = [10, 20, 30, 40, 50]

iterators = iter(numbers)

print(next(iterators, "No Value"))  # First cursor
print(next(iterators, "No Value"))  # Second cursor
print(next(iterators, "No Value"))  # Third cursor
print(next(iterators, "No Value"))  # Forth cursor
print(next(iterators, "No Value"))  # Fifth cursor
# 'No Value' if not found any object in that case
# default value will appearing instead of StopIteration raise Exception
print(next(iterators, "No Value"))  # Sixth cursor
print("-" * 100)

# Example 2:
# Tuple:
numbers = (10, 20)

iterators = iter(numbers)

print(next(iterators, "No Value"))
print(next(iterators, "No Value"))
print(next(iterators, "No Value"))

print("-" * 100)

# Example 3:
# String:

my_string = "Pradip"

iterators = iter(my_string)

print(next(iterators, "No Value"))
print(next(iterators, "No Value"))
print(next(iterators, "No Value"))
print(next(iterators, "No Value"))
print(next(iterators, "No Value"))
print(next(iterators, "No Value"))
print(next(iterators, "No Value"))

print("-" * 100)

# Example 4:
# Set:

my_set = {10, 20, 30}

iterators = iter(my_set)

print(next(iterators, "No Value"))
print(next(iterators, "No Value"))
print(next(iterators, "No Value"))
print(next(iterators, "No Value"))

print("-" * 100)

# Example 5:
# Dictionary:

my_dict = {"Name": "Pradip", "Age": 33}

iterator = iter(my_dict)

print(next(iterator, "No Value"))
print(next(iterator, "No Value"))
print(next(iterator, "No Value"))
print("-" * 50)

# By dict.items()

iterator = iter(my_dict.items())

print(next(iterator, "No Value"))
print(next(iterator, "No Value"))
print(next(iterator, "No Value"))

print("-" * 50)

# By dict.values()

iterator = iter(my_dict.values())

print(next(iterator, "No Value"))
print(next(iterator, "No Value"))
print(next(iterator, "No Value"))

print("-" * 50)

# By dict.keys()

iterator = iter(my_dict.keys())

print(next(iterator, "No Value"))
print(next(iterator, "No Value"))
print(next(iterator, "No Value"))

print("-" * 100)

# Example 6:
# range() :

numbers = range(1, 3)

iterators = iter(numbers)

print(next(iterators))
print(next(iterators))
print(next(iterators, "No Value"))
