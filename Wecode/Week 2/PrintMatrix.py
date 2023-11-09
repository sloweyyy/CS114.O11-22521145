r, c = map(int, input().split())

matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))

col_widths = [0] * c
for row in matrix:
    for j, val in enumerate(row):
        col_widths[j] = max(col_widths[j], len(str(val)))

for row in matrix:
    for j, val in enumerate(row):
        print(str(val).rjust(col_widths[j]), end=' ')
    print()