a = int(input())
b = int(input())
c = int(input())

if ((a < b + c) and (b < a + c) and (c < a + b)):
    p = 0.5 * (a + b + c)
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    if (a == b and b == c and a == c):
        print('Tam giac deu, dien tich = {}'.format(int(s) if round(s, 1) - int(s) == 0.0 else round(s, 2)))
    elif ((a == b) or (b == c) or (a == c)):
        print('Tam giac can, dien tich = {}'.format(int(s) if round(s, 1) - int(s) == 0.0 else round(s, 2)))
    elif ((a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (c ** 2 + b ** 2 == a ** 2)):
        print('Tam giac vuong, dien tich = {}'.format(int(s) if round(s, 1) - int(s) == 0.0 else round(s, 2)))
    else:
        print('Tam giac thuong, dien tich = {}'.format(int(s) if round(s, 1) - int(s) == 0.0 else round(s, 2)))
else:
    print('Khong phai tam giac')
