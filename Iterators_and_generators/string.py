"""Iterate over a string using an iterator."""


text = "Pradi p"

iterator = iter(text)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("Iterator is exhausted.")
        break
