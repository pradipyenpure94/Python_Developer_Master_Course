"""Program 4: Iterate Through a Dictionary."""

data = {"name": "Pradip", "age": 33}

dictionary_iterator = iter(data)

while True:
    try:
        key = next(dictionary_iterator)
        print(key, "==", data[key])
    except StopIteration:
        break
