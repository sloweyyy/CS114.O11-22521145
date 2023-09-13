n = int(input())
k = int(input())
p = int(input())
q = int(input())

vt_Bob = 2 * (p - 1) + q
if vt_Bob - k < 1 and n < vt_Bob + k:
    print(-1)
else:
    if vt_Bob - k >= 1:
        vt_Alice = vt_Bob - k
    elif vt_Bob + k <= n:
        vt_Alice = vt_Bob + k
    u = (vt_Alice - 1) // 2 + 1
    v = vt_Alice - 2 * (u - 1)
    print(u, v) 
