"""Find common element in two tuple."""
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

result = ()

for i in t1:
    if i in t2:
        result += (i, )

print(f"Common element: {result}")
