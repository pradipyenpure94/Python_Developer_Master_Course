"""Matrix addition."""

list1 = [[1, 2, 3], [4, 5, 6]]
list2 = [[4, 5, 3], [9, 5, 16]]

result = []
for i, _ in enumerate(list1):
    row = []
    for j, _ in enumerate(list1[0]):
        row.append((list1[i][j] + list2[i][j]))
    result.append(row)

print(f"Matrix addition: {result}")
