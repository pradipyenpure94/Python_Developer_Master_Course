"""Find common elements in two lists."""

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
prime = [2, 3, 5, 7, 11, 13, 17, 19]

odd_set = set(odd)
prime_set = set(prime)
common_elements = []

for number in odd_set:
    if number in prime_set:
        common_elements.append(number)

print(f"Common elements of two lists: {common_elements}")
