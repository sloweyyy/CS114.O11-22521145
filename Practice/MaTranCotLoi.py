import numpy as np


def find_one(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                return i, j
    return -1, -1


def manhattan_dist(i, j):
    return abs(i - 3) + abs(j - 3)


matrix = np.zeros((5, 5), dtype=int)

for i in range(5):
    row_str = " ".join(map(str, input().split()))
    matrix[i] = np.fromstring(row_str, dtype=int, sep=' ')

i, j = find_one(matrix)

dist = manhattan_dist(i, j)

print(dist)
