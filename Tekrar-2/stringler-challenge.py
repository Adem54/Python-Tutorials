# Bir stringin bir alt parçasını dönen alt_str adlı bir fonksiyon yazmak istiyoruz.
# Verilen string'in başlangıç ve bitiş indisleri arasındaki parçayı geri dönecek.
# Hesaplanan alt kümeye bitiş indisi dahil edilmeyecek.Yani,
# alt_str("merhaba", 0, 1) yazdığımızda "m" dönmeli.
# alt_str("merhaba", 2, 4) yazdığımızda "rh"

def alt_str(string, bas_indis, son_indis):
    yeni_string = ""
    while bas_indis < son_indis:
        eleman = string[bas_indis]
        yeni_string += eleman
        bas_indis += 1
    return yeni_string


print(alt_str("sakarya", 3, 5))

"""
Üç stringi bir birine ekleyerek return ile döndür
alt_str fonksiyonun kullanarak; string'in  başlangıcı ile kacinci arasını alınız.
yeni_karakter  ekleyiniz
alt_str kullanarak: string'in kacinci'dan bir sonraki karakteri ile string'nin sonuna kadar olan kısmı ekleyiniz.
"""


def karakter_degistir(string, kacinci, yeni_karakter):
    yeni_string = alt_str(string, 0, kacinci)
    yeni_string += yeni_karakter
    yeni_string += alt_str(string, kacinci + 1, len(string))
    return yeni_string


print(karakter_degistir("merhaba", 1, "x"))
