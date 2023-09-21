def can_transform(s, t):

    diff_count = sum(1 for i in range(len(s)) if s[i] != t[i])

    if diff_count % 2 == 0:
        return "YES"
    else:
        return "NO"


q = int(input())
results = []

for _ in range(q):
    s = input()
    t = input()
    result = can_transform(s, t)
    results.append(result)

for result in results:
    print(result)
