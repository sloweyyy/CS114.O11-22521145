n = int(input())
arr = list(map(int, input().split()))
k, x = map(int, input().split())

left = 0
right = n - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == x:
        break
    elif arr[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

result = []
i = mid - 1
j = mid
if arr[mid] != x:
    if i < 0:
        result = arr[j:j+k]
    elif j >= n:
        result = arr[i-k+1:i+1]
    else:
        if x - arr[i] <= arr[j] - x:
            result.append(arr[i])
            i -= 1
        else:
            result.append(arr[j])
            j += 1

while len(result) < k:
    if i < 0:
        result.extend(arr[j:j+k-len(result)])
    elif j >= n:
        result = arr[i-k+len(result)+1:i+1] + result
    else:
        if x - arr[i] <= arr[j] - x:
            result.append(arr[i])
            i -= 1
        else:
            result.append(arr[j])
            j += 1

for num in result:
    print(num, end=' ')
