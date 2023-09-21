s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("NO")
else:
    reversed_s1 = s1[::-1]
    if reversed_s1 == s2:
        print("YES")
    else:
        print("NO")