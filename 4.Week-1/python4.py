# Bir sayının karesini alan fonksiyona ihtiyacımız var

def karesi(sayi):
    return sayi * sayi


sayinin_karesi = karesi(15)
print(sayinin_karesi)


# Python içerisinde hazır gelen fonksiyonlar vardır input,print,int gibi.
# Bu tür fonksiyonlara built-in (önceden tanımlanmış) fonksiyonlar denilmektedir.


# Verilen bir sayının mutlak değerini hesaplayan bir fonksiyon yazılması isteniyor.

def mutlak_deger(x):
    if x < 0:
        return -1 * x
    else:
        return x


result = mutlak_deger(-5)
print(result)
