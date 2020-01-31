def selamla(isim):
    print("merhaba " + isim)


selamla("Ahmet")
selamla("Mehmet")


def dikdortgen_alan_hesapla(en, boy):
    alan = en * boy
    print("Dikdörtgenin alanı: " + str(alan))


dikdortgen_alan_hesapla(12, 4)

print("---------------------------------------------------------------------------------")


# Önceki adımlarda kullandığımız sayı okuma işlemini yapmak için şu şekilde bir fonksiyon tanımlayabiliriz:
def sayi_oku(mesaj):
    return int(input(mesaj))


taban = sayi_oku("Üçgenin tabanını giriniz:  ")
yukseklik = sayi_oku("Üçgenin yüksekliğini giriniz ")
print("Üçgenin Alanı: " + str(taban * yukseklik))


