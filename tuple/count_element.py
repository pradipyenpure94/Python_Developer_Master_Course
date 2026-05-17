"""Find element appearing only once."""

t = (1, 2, 2, 3, 5, 6, 4, 4, 5, 8)

for number in t:
    if t.count(number) == 1:
        print(number)
