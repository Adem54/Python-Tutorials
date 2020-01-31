# Verilen bir listedeki sayıların verilen bi kuvvetini alıp liste halinde dönen kuvvet_al bir fonksiyon yazın.

def kuvvet_al(liste, n):
    yeni_liste = []
    for eleman in liste:
        yeni_liste.append(eleman ** n)
    return yeni_liste


print(kuvvet_al([2, 3, 4, 5, 6], 5))
