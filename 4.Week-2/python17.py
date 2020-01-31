# Tekrar eden değerleri listeden çıkaran fonksiyon

def ben_ne_yapiyorum(liste):
    indis = 0
    yeni_liste = []
    while indis < len(liste):
        eleman = liste[indis]
        if eleman not in yeni_liste:
            yeni_liste.append(eleman)
        indis = indis + 1

    return yeni_liste


print(ben_ne_yapiyorum([11, "ali", [11], 11, "veli", "11"]))
