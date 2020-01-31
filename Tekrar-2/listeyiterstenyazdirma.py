liste = [12, 3, 14, 56, 21, 11, 9]


def liste_tersten_yazdir(list):
    new_list = []
    sayac = len(list) - 1
    while 0 <= sayac:
        eleman = list[sayac]
        new_list.append(eleman)
        sayac -= 1
    return new_list


liste = [12, 3, 14, 56, 21, 11, 9]
print(liste_tersten_yazdir(liste))


def tersten_yazdir(list):
    new_list = []
    for sayi in range(len(list)):
        eleman = list.pop()
        new_list.append(eleman)
    return new_list


liste = [12, 3, 14, 56, 21, 11, 9]
print(tersten_yazdir(liste))
