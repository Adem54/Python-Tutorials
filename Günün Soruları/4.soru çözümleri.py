def my_len(liste):
    i = 0
    for eleman in liste:
        i = i + 1
    return i


def my_append(liste, new_eleman):
    return liste + [new_eleman]


def my_insert(liste, index, eleman):
    return liste[:index] + [eleman] + liste[index:]


def my_pop(liste, index):
    i = 0
    for eleman in liste:
        i = i + 1
    if index == " ":
        index = i - 1
    silinen_eleman = liste[index]
    liste = liste[:index] + liste[index + 1:]
    return [liste, silinen_eleman]


def my_remove(liste, eleman):
    if eleman not in liste:
        print("eleman listede yok")
    else:
        i = 0
        index = 0
        for member in liste:
            i = i + 1
            if member == eleman:
                index = i - 1
                return liste[:index] + liste[index + 1:]



def my_index(liste, eleman):
    if eleman not in liste:
        print("eleman listede yok")
    else:
        i = 0
        index = 0
        for member in liste:
            i = i + 1
            if member == eleman:
                index = i - 1
                return index


liste = ["d", 2, "a", "c", 93, 6]
print(my_len(liste))
liste = ["d", 2, "a", "c", 93, 6]
print(my_append(liste, 7))
liste = ["d", 2, "a", "c", 93, 6]
print(my_insert(liste, 3, "abc"))
liste = ["d", 2, "a", "c", 93, 6]
print(my_pop(liste, 2))
liste = ["d", 2, "a", "c", 93, 6]
print(my_remove(liste, "c"))
liste = ["d", 2, "a", "c", 93, 6]
print(my_index(liste, 2))
