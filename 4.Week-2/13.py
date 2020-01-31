# string lerin listelerden farkı stringlerin herhangi bir karakteri liste içindeki elemanı
# değiştirdiğmiz gibi değiştemeyiz


# liste = ["m", "e", "r", "h", "a", "b", "a"]
# string = "merhaba"
# print(len(liste))  # ekrana 7 yazar
# print(len(string))  # ekrana 7 yazar
# liste[3] = "l"
# string[3] = "l"  # Hata verir


# String'lerin içindeki değerin, listelerdeki gibi değiştirilemediğini öğrenmiştik. Bu yüzden, doğrudan
# bir string'in içeriğini değiştirmek yerine, "istenilen değişikliği içeren yeni bir string" oluşturmak gerekir

# string e eleman eklemek concetanation gibi + ile eleman ekleyebiliriz...
def karakter_degistir(string, kacinci, yeni_karakter):
    yeni_string = ""
    indis = 0
    # burda bir string in karakterlerini girer kacıncı karaktere kadar yazarsak
    while indis < kacinci:
        yeni_string += string[indis]

        indis += 1
        # burda ise yeni_string i ekler
    yeni_string += yeni_karakter
    indis += 1

    while indis < len(string):
        yeni_string += string[indis]
        indis += 1
    return yeni_string


# yeni_string = karakter_degistir("merhaba", 0, "x")  # xerhaba sonucunu verir
# yeni_string = karakter_degistir(yeni_string, 1, "y")
# bu fonksiyon çalışınca yeni_string xerhaba idi 1.indisdeki karakteri e dir e yi "y" ile değiştir diyor ve
# bu arada 1. indis olduğunda indis 1 artıyor birde indis yeni karakter "y" yi eklerken artıyor dolayısı ile
# en altta string in değerlerini girerken indis 2 den başlıyor ondan dolayı string in 3.indisinden itibaren(0,1,2)
# yani 2.demek oluyor almaya başlar
# yeni_string = karakter_degistir(yeni_string, 2, "z")
# print(yeni_string)

print(karakter_degistir("merhaba", 1, "x"))
