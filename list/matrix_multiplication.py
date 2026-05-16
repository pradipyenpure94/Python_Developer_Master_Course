"""Matrix multiplication."""

Matrix_A = [[1, 2, 3], [4, 5, 6]]
Matrix_B = [[7, 8], [9, 10], [11, 12]]

result = []

for i, _ in enumerate(Matrix_A):
    row = []
    for j, _ in enumerate(Matrix_B[0]):
        total = 0
        for k, _ in enumerate(Matrix_B):
            total += Matrix_A[i][k] * Matrix_B[k][j]
        row.append(total)
    result.append(row)
print(f"Matrix multiplication: {result}")
