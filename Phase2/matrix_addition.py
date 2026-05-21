"""Matrix addition using nested lists."""

x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
print(f"Matrix addition: {result}")
