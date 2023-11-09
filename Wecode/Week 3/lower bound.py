import array

n = int(input())
arr = array.array('i', [int(x) for x in input().split()])
m = int(input())
queries = array.array('i', [int(x) for x in input().split()])

for q in queries:
    idx = arr.index(q) if q in arr else -1
    print(idx)
