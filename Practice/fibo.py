n = int(input())

if (n < 1 or n > 30):
    print('So {} khong nam trong khoang [1,30].'.format(int(n)))
else:
    print(int(1 / (5 ** 0.5) * (((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n)))
