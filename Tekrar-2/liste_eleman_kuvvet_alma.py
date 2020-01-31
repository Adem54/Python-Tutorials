"""
Verilen bir listedeki sayıların, belirtilen bir kuvvetini alıp, yine liste halinde dönen
kuvvet_al adında bir fonksiyon yazın.
kuvvet_al([1, 2, 3], 3) şeklinde çağrıldığında sonuç olarak [1, 8, 27] dönmeli
"""


def kuvvet_al(liste, kuvvet):
    new_list = []
    for eleman in liste:
        new_list.append(eleman ** kuvvet)
    return new_list


listem = [2, 3, 4]
print(kuvvet_al(listem, 3))
