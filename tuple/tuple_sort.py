"""Tuple sorting without sort()"""

t = (5, 1, 9, 3, 7)

lst = list(t)
length_lst = len(lst)

count = 0
for i in range(length_lst):
    for j in range(length_lst - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            count += 1

print(f"Sorted numbers: {tuple(lst)}")
