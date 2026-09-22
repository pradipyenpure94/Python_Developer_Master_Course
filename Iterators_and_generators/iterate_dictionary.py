"""
Create an iterator from Dictionary.

Iterate Over:
    - keys
    - values
    - key-value pairs
"""


data = {"name": "Pradip", "age": 33}

# Iterate over keys
print("Iterate Over keys: ")

key_iterator = iter(data)

for key in key_iterator:
    print(key)

# Iterate over values
print("\nIterate over values: ")

value_iterator = iter(data.values())

for value in value_iterator:
    print(value)

# Iterate over key-value pairs
print("\nIterate over key-value pairs: ")
iterator_key_value_pairs = iter(data.items())

for key, value in iterator_key_value_pairs:
    print(key, ":", value)
