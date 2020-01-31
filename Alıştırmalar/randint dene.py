from random import randint

liste = ["a", 4, "d", "elma", "armut", 13, True]
"""
sayac = 0
yeni_liste = []
while sayac < 3:
    rastgele_sayi = randint(0, len(liste))
    rastgele_eleman = yeni_liste.append(liste[rastgele_sayi])
    sayac += 1
print(yeni_liste)

"""


def diziden_rastgelen_eleman_sec(secilecek_eleman_sayisi, secilecek_liste):
    new_list = []
    sayac = 1
    while sayac <= secilecek_eleman_sayisi:
        random_number = randint(0, len(secilecek_liste))
        eklenen_random_eleman = secilecek_liste[random_number]
        if eklenen_random_eleman in new_list:
            new_list
        else:
            new_list.append(eklenen_random_eleman)

        sayac += 1
    return new_list


liste = ["a", 4, "d", "elma", "armut", 13, True]
print(diziden_rastgelen_eleman_sec(5, liste))
