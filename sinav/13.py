"""
Verilen bir listede, n defa tekrar eden sayıları liste halinde dönen fonksiyonu yazınız.

Ornek: [1,1,2,2,2,3,4,4,4,4,5,5,6,7,5] listesinde üç defa tekrar eden elemanlar [2,5] tir.

Not: Sonucun sıralı dönmesi için, yine liste.sort() fonksiyonunu kullanın
"""


def itemsThatOccurNTimes(numbers, n):
    uniq_list = []
    for eleman in numbers:
        if eleman not in uniq_list:
            uniq_list.append(eleman)

    liste_tekrar = []
    for sayi in range(len(uniq_list)):
        eleman1 = uniq_list[sayi]
        count = 0

        for eleman2 in numbers:

            if eleman1 == eleman2:
                count += 1
        if count == n:
            liste_tekrar.append(eleman1)
    return liste_tekrar


print(itemsThatOccurNTimes([1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 5], 2))
print(itemsThatOccurNTimes([1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 5], 3))
print(itemsThatOccurNTimes([1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 5], 4))
