liste = [12, 3, 14, 56, 21, 11, 9]

"""
Listedeki en büyük ve en küçük elemanı bulma
"""


def listedeki_en_buyuk_sayi(list):
    en_buyuk_eleman = 0
    en_kucuk_eleman = 1000
    new_list = []
    for eleman in list:
        if eleman > en_buyuk_eleman:
            en_buyuk_eleman = eleman
        if eleman < en_kucuk_eleman:
            en_kucuk_eleman = eleman

    new_list.append(en_kucuk_eleman)
    new_list.append(en_buyuk_eleman)
    return new_list


print(listedeki_en_buyuk_sayi(liste))
