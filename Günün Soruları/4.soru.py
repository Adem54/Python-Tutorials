"""
Listelerle ilgili gordugumuz methodlarla ayni isi yapan, asagidaki fonsiyonlari yaziniz
Soru cozulurken listelerle ilgili hic bir method veya fonksiyon  kullanilmamalidir.
my_len(liste)------> listedeki eleman sayisini geri doner
my_append(liste, eleman)----> eleman'i listenin sonuna ekler ve listeyi geri doner
my_insert(liste, index, eleman) ----> listede index'e elemani ekler ve listeyi geri doner
my_pop (liste, index) ----> index'teki elemani siler ve silinen elemani geri doner, my_pop(liste, ' ') seklinde
 cagirilirsa, listenin son elemanini siler ve geri doner.
my_remove(liste, eleman) -----> elemani listeden siler ve listeyi geri doner, eleman listede birden fazlaysa
 sadece ilk elemani siler, eleman listede yoksa ekrana "eleman listede yok" hatasi yazdirir,
my_index (liste, eleman) ----> elemanin indexini geri doner. eleman listede birden fazla yer aliyorsa sadece
ilk elemanin indexini doner.
"""

# 1)Listedeki eleman sayısını geri dönen fonksiyonu len methodu kullanmadan yazınız
liste = [1, 3, "Ahmet", 12, True]


def my_len(liste):
    eleman_sayisi = 0

    for sayi in liste:
        eleman_sayisi += 1
    return eleman_sayisi


print(my_len(liste))

# 2)my_append(liste, eleman)----> eleman'i listenin sonuna ekler ve listeyi geri doner

liste = [1, 3, "Ahmet", 12, True]


def my_append(liste, eleman):
    liste = liste + [eleman]
    return liste


# my_append(liste, "Kamil")
# print(liste)
print(my_append(liste, "Kamil"))


# 3) my_insert(liste, index, eleman) ----> listede index'e elemani ekler ve listeyi geri doner
def my_insert(liste, index, eleman):
    liste[index:index:1] = [eleman]
    return liste


liste = ["Kayahan", 23, 54, False, "Serdar"]

print(my_insert(liste, 2, 345))

# my_pop (liste, index) ----> index'teki elemani siler ve silinen elemani geri doner, my_pop(liste, ' ') seklinde
liste1 = ["Kayahan", 23, 54, False, "Serdar"]


def my_pop(liste, index):
    liste = liste[0:index] + liste[index + 1:]
    return liste[index]


print(my_pop(liste1, 2))
print(liste1)

"""
my_remove(liste, eleman) -----> elemani listeden siler ve listeyi geri doner, eleman listede birden fazlaysa
 sadece ilk elemani siler, eleman listede yoksa ekrana "eleman listede yok" hatasi yazdirir,
"""


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


"""
my_index (liste, eleman) ----> elemanin indexini geri doner. eleman listede birden fazla yer aliyorsa sadece
ilk elemanin indexini doner.
"""


def my_index(liste, eleman):
    if eleman in liste:
        index = -1
        new_list = []
        for member in liste:
            index += 1
            if member == eleman:
                return index # return yaptığımız için ilk elemanda bulur bulamz onu döndürür ve return edince
                # zaten bitirmiş olur return işlemleri ama bize birden fazla varsa o zaman son eleman ı al dese idi
                # o zaman return ile olmazdı bu işlem o zamanda biz bulduğumuz indexleri bir dizi içersiine atıp
                # ordan alırdık



my_list = [1, 5, 3, 6, 5, 3, 5, 4, 6, 1, 4, 3, 5]
print(my_index(my_list, 4))
