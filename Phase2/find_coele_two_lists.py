"""Find common elements in two lists."""

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
prime = [2, 3, 5, 7, 11, 13, 17, 19]

prime_set = set(prime)
common_elements = []
index = 0
odd_list = list(set(odd))


while index < len(odd_list):
    current_number = odd_list[index]
    if current_number in prime_set:
        common_elements.append(current_number)
    index += 1

print(f"Common elements of two lists: {common_elements}")
