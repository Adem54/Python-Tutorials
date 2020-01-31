"""
2 tane liste'yi parameter olarak alan, bu listeleri birlestirerek tek bir liste olusturan ve olusan
bu listeyi geri donen merge(liste1, liste2) fonksiyonunu yaziniz.
merge fonksiyonun geri donecegi listede bir eleman birden fazla yer almamali, yani bir eleman
hem liste1 hem de liste2'de yer aliyorsa, bu eleman olusturulacak listeye sadece 1 kez eklenmeli.

liste1= [2, 5 ,6 ,7 , 10]
liste2= [5, 6, 9, 8]

print(merge(liste1, liste2))
[2, 5, 6, 7, 10, 9, 8]
Peki aynı liste içerisinde tekrar eden değerler  olursa ne olacak...
"""


def merge(liste1, liste2):
    yeni_liste = []
    for eleman1 in liste1:
        if eleman1 not in yeni_liste:
            yeni_liste.append(eleman1)
    for eleman2 in liste2:
        if eleman2 not in yeni_liste:
            yeni_liste.append(eleman2)

    return yeni_liste


liste1 = [2, 5, 2, 6, 7, 10]
liste2 = [5, 6, 6, 9, 5, 8]
print(merge(liste1, liste2))
