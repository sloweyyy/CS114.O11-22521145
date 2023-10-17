from sys import stdin
from collections import deque

dq = deque()

while True:
    line = stdin.readline().split()
    cmd = int(line[0])

    if cmd == 0:
        dq.appendleft(int(line[1]))

    elif cmd == 1:
        dq.append(int(line[1]))

    elif cmd == 2:
        x, y = int(line[1]), int(line[2])
        if x in dq:
            dq.insert(dq.index(x)+1, y)
        else:
            dq.appendleft(y)

    elif cmd == 3:
        x = int(line[1])
        if x in dq:
            dq.remove(x)

    elif cmd == 4:
        x = int(line[1])
        dq = deque(i for i in dq if i != x)

    elif cmd == 5:
        if dq:
            dq.popleft()

    elif cmd == 6:
        break

if dq:
    print(*dq)
else:
    print("blank")
