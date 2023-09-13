from decimal import Decimal, getcontext

getcontext().prec = 6


def F_to_C_and_K(temp_F):
    temp_F = Decimal(temp_F)
    temp_C = (temp_F - 32) * 5 / 9

    temp_K = temp_C
    temp_K += Decimal(273.15)

    return f"{temp_C} {temp_K}"


if __name__ == '__main__':
    temp_F = input()
    print(F_to_C_and_K(temp_F))
