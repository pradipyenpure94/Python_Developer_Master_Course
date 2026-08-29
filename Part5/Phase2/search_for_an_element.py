"""Search for an element."""

even_numbers = [2, 4, 6, 8, 10]
search_element = 4
index = 0
found = False

while index < len(even_numbers):
    if search_element == even_numbers[index]:
        found = True
        break
    index += 1

if found:
    print(f"{search_element} element is found.")
else:
    print(f"{search_element} element is not found.")

