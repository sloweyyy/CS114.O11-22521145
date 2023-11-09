import collections
from sys import stdin

arr = collections.deque()
result = []

while True:
    a = [int(x) for x in stdin.readline().split()]
    if a[0] == 0:
        arr.appendleft(a[1])
    elif a[0] == 1:
        arr.append(a[1])
    elif a[0] == 2:
        try:
            index = arr.index(a[1]) + 1
            arr.insert(index, a[2])
        except:
            arr.appendleft(a[2])
    elif a[0] == 3:
        try:
            index = arr.index(a[1])
            arr.remove(a[1])
        except:
            pass
    elif a[0] == 4:
        arr = collections.deque(filter(lambda i: i != a[1], arr))
    elif a[0] == 5:
        if len(arr) != 0:
            arr.popleft()
    elif a[0] == 6:
        result.extend(arr)
        break

if len(result) != 0:
    print(*result)
else:
    print("blank")
