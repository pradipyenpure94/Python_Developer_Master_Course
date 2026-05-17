"""Find common elements in two tuple."""

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

result = ()
index = 0

while index < len(t1):
    current_number = t1[index]
    if current_number in t2:
        result += (current_number, )
    index += 1

print(f"Common elements: {result}")
