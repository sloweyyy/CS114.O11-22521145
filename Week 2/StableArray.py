def min_stability(arr):
    n = len(arr)
    arr.sort()

    if n == 2:
        return 0
    else:
        return min(arr[n - 2] - arr[0], arr[n - 1] - arr[1])


n = int(input())
arr = list(map(int, input().split()))

result = min_stability(arr)
print(result)
