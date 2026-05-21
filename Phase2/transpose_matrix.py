"""Transpose matrix."""

x = [[12, 7],
     [4, 5],
     [3, 8]
     ]

row, col = len(x), len(x[0])
result = [[x[i][j] for i in range(row)] for j in range(col)]
print(f"Transpose Matrix: {result}")
