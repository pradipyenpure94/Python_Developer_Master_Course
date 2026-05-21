"""Matrix addition using nested lists."""

x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = []

for i, _ in enumerate(len(x)):
    row = []
    for j in range(len(x[0])):
        row.append((x[i][j] + y[i][j]))
    result.append(row)

print(f"Matrix addition: {result}")
