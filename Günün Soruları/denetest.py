from random import randint


def kelime_uret():
    kelime_liste = ["kodstar", "programci", "kaptan", "merhaba", "python", "kemal", "mustafa", "sakarya", "yilbasi",
                    "karanlik"]
    rand = randint(0, 9)
    kelime = kelime_liste[rand]
    tahmin_edilen_kelime = []
    for character in kelime:
        tahmin_edilen_kelime.append(character)
    return tahmin_edilen_kelime


tahmin_durumu = kelime_uret()
tahmin_edilen_kelime_durumu = []

for karakter in tahmin_durumu:
    tahmin_edilen_kelime_durumu.append("")

print(tahmin_edilen_kelime_durumu)
print(tahmin_durumu)

deneme_sayisi = 8
alfabe = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "y", "z"]
copy_alfabe = alfabe[:]
tahmin_edilen_harfler = []
dogru_tahmin_edilen_harfler = []
while deneme_sayisi > 0:

    harf = input("Lutfen bir harf tahmin edin: ")
    tahmin_edilen_harf = harf.lower()
    if tahmin_edilen_harf not in copy_alfabe:
        harf = input("Lutfen alfabe içinde olan bir harf tahmin edin: ")
        tahmin_edilen_harf = harf.lower()

    tahmin = False

    if len(tahmin_edilen_harfler) > 0 and tahmin_edilen_harf in tahmin_edilen_harfler:
        deneme_sayisi = deneme_sayisi
        print("Aynı harfi daha önce tahmin ettiğiniz için deneme sayısı: " + str(deneme_sayisi))
    else:
        for sayi in range(len(tahmin_durumu)):
            char = tahmin_durumu[sayi]

            if tahmin_edilen_harf == char:
                print("sayi: " + str(sayi))
                print("char: " + str(char))

                tahmin_edilen_kelime_durumu[sayi] = char
                dogru_tahmin_edilen_harfler.append(char)

                tahmin = True
            else:
                tahmin = tahmin

            if tahmin and sayi == (len(tahmin_durumu) - 1):
                print("Iyi tahmin: " + str(tahmin_edilen_kelime_durumu))
            elif sayi == (len(tahmin_durumu) - 1):
                print("Oops! Yanlis tahmin: " + str(tahmin_edilen_kelime_durumu))

            if sayi == (len(tahmin_durumu) - 1):
                tahmin_edilen_harfler = tahmin_edilen_harfler + [tahmin_edilen_harf]
                print("Tahmin ettiğniz harfler: " + str(tahmin_edilen_harfler))
                alfabe.remove(tahmin_edilen_harf)
                print("Alfabede Kalan Harfler: " + str(alfabe))

        if tahmin:

            deneme_sayisi = deneme_sayisi
            print(str(deneme_sayisi) + " tahmin hakkınız kaldı")
        else:
            deneme_sayisi -= 1
            print(str(deneme_sayisi) + " tahmin hakkınız kaldı")
        if deneme_sayisi >= 0 and len(dogru_tahmin_edilen_harfler) == len(tahmin_durumu):
            print("Tebrikler tüm harfleri " + str(8 - deneme_sayisi) + " hakta bildiniz ve oyunu kazandınız")
            break
        elif deneme_sayisi == 0 and len(dogru_tahmin_edilen_harfler) != len(tahmin_durumu):
            print("Malesef " + str(8 - deneme_sayisi) + " hakkınız doldu harfleri tamamlayamadınız")
