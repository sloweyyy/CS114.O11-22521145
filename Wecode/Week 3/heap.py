import heapq

n, m = map(int, input().split())
arr = []

for _ in range(n):
    heapq.heappush(arr, -int(input()))

max_value = -arr[0]

for _ in range(m):
    operation = input().split()
    if operation[0] == '-1':
        heapq.heappop(arr)
        if not arr:
            max_value = 0
        else:
            max_value = -arr[0]
    elif operation[0] == '-2':
        new_arr = []
        for x in arr:
            if x != -max_value:
                heapq.heappush(new_arr, x)
        arr = new_arr
        if not arr:
            max_value = 0
        else:
            max_value = -arr[0]
    elif operation[0] == '-3':
        new_arr = []
        for x in arr:
            if x == -max_value:
                heapq.heappush(new_arr, x + int(operation[1]))
            else:
                heapq.heappush(new_arr, x)
        arr = new_arr
        max_value = -arr[0]
    elif operation[0] == '-4':
        decrement = int(operation[1])
        new_arr = []
        for x in arr:
            if x == -max_value:
                heapq.heappush(new_arr, x - decrement)
            else:
                heapq.heappush(new_arr, x)
        arr = new_arr
        max_value = -arr[0]

arr.sort(reverse=False)

for num in arr:
    print(-num)
