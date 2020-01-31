def mutlak_deger(x):
    if x < 0:
        return x * -1
    elif x > 0 or x == 0:
        return x


print(mutlak_deger(-4))

print("----------------------------------------------")


def faktoryel_hesapla(sayi):
    faktoryel = 1
    while sayi > 0:
        faktoryel = faktoryel * sayi
        sayi -= 1
    return faktoryel


print(faktoryel_hesapla(4))
