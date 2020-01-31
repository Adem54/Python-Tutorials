liste = [12, 3, 14, 56, 21, 11, 9]


def liste_kuvvet_alma(list, kuvvet):
    new_list = []
    for eleman in list:
        new_eleman = eleman ** kuvvet
        new_list.append(new_eleman)
    return new_list


print(liste_kuvvet_alma(liste, 2))
