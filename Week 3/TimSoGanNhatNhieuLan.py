import sys
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

def find_closest_k(arr, x, k):
    len_arr = len(arr)
    index_find = bisect_left(arr, x, 0, len_arr - 1)
    left = max(0, index_find - k + 1)
    right = k + left - 1
    while right + 1 < len_arr and arr[right + 1] - x < x - arr[left]:
        left += 1
        right += 1
    return arr[left], arr[right]

while True:
    try:
        line = input()
        if not line:
            break
        k, x = map(int, line.split())
        min_val, max_val = find_closest_k(arr, x, k)
        print(min_val, max_val)
    except EOFError:
        break
