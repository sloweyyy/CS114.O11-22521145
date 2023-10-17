import sys

n = int(input())
arr = (int(x) for x in input().split())
m = int(input())
queries = (int(x) for x in input().split())

def lower_bound(arr, x):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

for q in queries:
    idx = lower_bound(arr, q)
    if idx < n and next(x for i, x in enumerate(arr) if i == idx) == q:
        print(idx)
    else:
        print(-1)
