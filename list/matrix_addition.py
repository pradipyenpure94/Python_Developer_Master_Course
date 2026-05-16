"""Matrix addition."""

list1 = [[1, 2, 3], [4, 5, 6]]
list2 = [[4, 5, 3], [9, 5, 16]]

result = []
i = 0

while i < len(list1):
    row = []
    j = 0

    while j < len(list1[0]):
        row.append((list1[i][j] + list2[i][j]))
        j += 1
    i += 1

    result.append(row)

print(f"Matrix addition: {result}")
