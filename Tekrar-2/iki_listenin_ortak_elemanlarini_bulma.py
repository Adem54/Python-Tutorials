"""
Verilen iki listenin ortak elemanlarını bulan kesisim adında bir fonksiyon yazın.
[2,3, 4, 5, 6] ile [32,23, 4, 15, 6] listesinin kesişimi için sonuç olarak [4,6] dönmesi gerekiyor.
"""


def kesisim(liste1, liste2):
    kesisim_liste = []
    for eleman1 in liste1:
        if eleman1 in liste2:
            kesisim_liste.append(eleman1)
    return kesisim_liste


print(kesisim([2, 3, 4, 5, 6], [32, 23, 4, 15, 6]))
