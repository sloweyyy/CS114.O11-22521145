def equal_strings(s, t):
    return s == t


def replace_char(s, i, j):
    return s[:i] + s[j] + s[i + 1:]


def transform_string(s, t):
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                return replace_char(s, i, j)
    return None


q = int(input())
for _ in range(q):
    s = input()
    t = input()
    if equal_strings(s, t):
        print("YES")
    else:
        transformed_s = transform_string(s, t)
        if transformed_s:
            print("YES")
        else:
            print("NO")
