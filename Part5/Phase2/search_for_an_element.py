"""Search for an element."""

even_numbers = [2, 4, 6, 8, 10]
search_element = 41

found = False

for number in even_numbers:
    if number == search_element:
        found = True
        break

if found:
    print(f"{search_element} element is found.")
else:
    print(f"{search_element} element is not found.")
