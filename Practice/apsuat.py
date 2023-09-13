from decimal import *

psi = float(input())

kgscm = 0.453592 / 2.54 ** 2 * psi

getcontext().prec = 6

print(Decimal(kgscm).normalize())
