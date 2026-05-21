"""Transpose matrix."""

x = [[12, 7],
     [4, 5],
     [3, 8]
     ]

row, col = len(x), len(x[0])
result = [[0] * row for _ in range(col)]

for i in range(row):
    for j in range(col):
        result[j][i] = x[i][j]

print(f"Transpose Matrix: {result}")
