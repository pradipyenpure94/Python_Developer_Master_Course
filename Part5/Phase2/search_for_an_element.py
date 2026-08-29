"""Search for an element."""

even_numbers = [2, 4, 6, 8, 10]
search_element = 4

found = True if search_element in even_numbers else False

if found:
    print(f"{search_element} element is found.")
else:
    print(f"{search_element} element is not found.")
