import bisect

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

for q in queries:
    idx = bisect.bisect_left(arr, q)
    if idx < n and arr[idx] == q:
        print(idx)
    else:
        print(-1)
