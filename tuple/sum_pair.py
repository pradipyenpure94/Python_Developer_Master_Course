"""Find pairs with target sum"""

t = (2, 4, 6, 3, 7, 8)
target = 10

for i, value in enumerate(t):
    for j in range(i+1, len(t)):
        if value + t[j] == target:
            print((value, t[j]))
