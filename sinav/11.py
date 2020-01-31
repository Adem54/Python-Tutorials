"""
Aşağıdaki şekilde takımlar ve takımların ligde yaptığı maçlarda aldığı sonuçların olduğu
listeyi parametre olarak alıp, geriye takımların toplam puanlarına aşağıdaki şekilde başka bir
 liste olarak dönen  toplam_puan fonksiyonunu yazınız.

Fonksiyonumuz takım sayısı ve maç sayısından bağımsız olarak çalışmalı,
yani sonuçlar listesinde kaç takım olursa olsun ve bu takımlar kaç maç yapmıs olurlarsa olsunlar çalışmalı.


G = 3 puan
B = 1 puan
M = 0 puan

Örnek:

sonuclar = [["Fenerbahce", "GGGBM"], ["Galatasaray", "GBBMG"], ["Besiktas", "BMBGB"]]

Çıktı:

[["Fenerbahce", 10], ["Galatasaray", 8], ["Besiktas", 6] ]
"""

""" """


def toplam_puanlar(sonuclar):
    liste_total = []
    for takimlar in sonuclar:
        liste = []
        for sayi in range(len(takimlar)):
            takim = takimlar[0]

            sonuc = takimlar[1]
            puan = 0
            for eleman in sonuc:

                if eleman == "G":
                    puan += 3
                elif eleman == "B":
                    puan += 1
                else:
                    puan += 0
        liste.append(takim)
        liste.append(puan)
        liste_total.append(liste)
    return liste_total


fbSonuclar = input("Fenerbahçe'nin 5 maçtaki sonucunu gir (örnek: GGBBM):")
gsSonuclar = input("Galatasaray'ın 5 maçtaki sonucunu gir:")
bjkSonuclar = input("Besiktas'ın 5 maçtaki sonucunu gir:")

puanlar = [["Fenerbahce", fbSonuclar], ["Galatasaray", gsSonuclar], ["Besiktas", bjkSonuclar]]
print(toplam_puanlar(puanlar))

"""
sonuc = "GGBBM"
puan = 0
for eleman in sonuc:

    if eleman == "G":
        puan += 3
    elif eleman == "B":
        puan += 1
    else:
        puan += 0

print(puan)
"""
