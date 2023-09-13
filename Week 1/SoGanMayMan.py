def is_lucky(n):
    return str(n).count('4') + str(n).count('7') == len(str(n))


def is_nearly_lucky(n):
    return is_lucky(str(n).count('4') + str(n).count('7'))


num = int(input())
if is_nearly_lucky(num):
    print("YES")
else:
    print("NO")
