def kuvvet_kopyala(liste, kuvvet):
    yeniliste = []
    for eleman in liste:
        yeniliste.append(eleman ** kuvvet)
    return yeniliste


orjinal = [1, 2, 3, 4, 5]
kopya = kuvvet_kopyala(orjinal, 2)
print(kopya)
