def is_diagonal_matrix(matrix):
    n = len(matrix)
    is_main_diagonal = all(matrix[i][i] == 1 for i in range(n))
    is_secondary_diagonal = all(matrix[i][n - i - 1] == 1 for i in range(n))
    is_zero = all(matrix[i][j] == 0 for i in range(n) for j in range(n) if i != j and i + j != n - 1)
    return (is_main_diagonal or is_secondary_diagonal) and is_zero


n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
if is_diagonal_matrix(matrix):
    print("YES")
else:
    print("NO")
