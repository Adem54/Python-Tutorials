def alt_str(string, baslangic, bitis):
    alt = ""
    indis = baslangic

    while indis < bitis:
        alt += string[indis]
        indis += 1

    return alt


def karakter_degistir(string, kacinci, yeni_karakter):
    yeni_string = alt_str(string, 0, kacinci)

    yeni_string += yeni_karakter

    yeni_string += alt_str(string, kacinci + 1, len(string))

    return yeni_string
    # alt_str fonksiyonunu kullanarak yazın


print(karakter_degistir("merhaba", 1, "x"))
