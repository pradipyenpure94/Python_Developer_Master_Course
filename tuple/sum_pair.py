"""Find pairs with target sum"""

t = (2, 4, 6, 3, 7, 8)
target = 10

i = 0
while i < len(t):
    j = 0
    while j < len(t):
        if t[i] + t[j] == target:
            print((t[i], t[j]))
        j += 1
    i += 1
