from math import ceil

n, m, a = map(int, input().split())
print(int(ceil(n / a) * ceil(m / a)))
