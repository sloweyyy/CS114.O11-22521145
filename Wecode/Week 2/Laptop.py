n = int(input())
a = list(map(int, input().split()))

a.sort()

min_missing = 0
expected = a[0]

for i in range(n):
    if a[i] == expected:
        expected += 1
    else:
        min_missing += a[i] - expected
        expected = a[i] + 1

print(min_missing)