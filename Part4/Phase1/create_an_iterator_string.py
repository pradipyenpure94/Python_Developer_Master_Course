"""Program 3: Create an Iterator for a String."""

text = "Pradip"

text_iterator = iter(text)

while True:
    try:
        print(next(text_iterator))
    except StopIteration:
        break
