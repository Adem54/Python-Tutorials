"""
Verilen iki liste arasındaki farklı elemanları bulan ve bunlardan yeni bir liste oluşturan program yazınız.

Örnek:

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

Çıktı:

[1, 2, 5, 6]
"""
def farkli_elemanlari_bul(liste1, liste2):
    liste = []
    for eleman1 in liste1:
        if eleman1 not in liste2:
            liste.append(eleman1)
    for eleman2 in liste2:
        if eleman2 not in liste1:
            liste.append(eleman2)
    return liste

print(farkli_elemanlari_bul([1, 2, 3, 4], [3, 4, 5, 6]))