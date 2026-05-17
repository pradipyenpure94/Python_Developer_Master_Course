"""Find element appearing only once."""

t = (1, 2, 2, 3, 5, 6, 4, 4, 5, 8)

index = 0

while index < len(t):
    current_number = t[index]
    if t.count(current_number) == 1:
        print(current_number)
    index += 1
