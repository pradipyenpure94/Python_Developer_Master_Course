"""Transpose matrix."""

x = [[12, 7],
     [4, 5],
     [3, 8]
     ]

row, col = len(x), len(x[0])
result = [[0] * row for _ in range(col)]

i = 0

while i < row:
    j = 0

    while j < col:
        result[j][i] = x[i][j]

        j += 1

    i += 1

print(f"Transpose Matrix: {result}")
