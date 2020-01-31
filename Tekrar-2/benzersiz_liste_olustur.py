def benzersiz_liste(liste):
    yeni_liste = []
    for eleman in liste:
        if eleman not in yeni_liste:
            yeni_liste.append(eleman)
    return yeni_liste


list = [5, 6, 8, 5, 6, 8, "ali", "veli", "ali", "veli"]
print(benzersiz_liste(list))
