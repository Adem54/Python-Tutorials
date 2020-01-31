"""
Bir fonksiyon yazın, parametre olarak bir liste ve n alsın.

Listeyi, n sayıda elemanı olan küçük listelere bölsün ve küçük listeleri döndürsün.
 Programınız o fonksiyonu kullanarak büyük bir listeyi parçalara bölsün ve ekrana yazdırsın.

Örnek: [1,2,3,4,5,6] listesini n=2 olan parcalara bolunce [[1,2]. [3,4],[5,6]] cikar.
"""


def splitList(listToSplit, n):
    liste1 = []
    liste2 = []
    counter = 1
    for eleman in listToSplit:
        liste2.append(eleman)
        if counter == n:
            liste1.append(liste2)
            liste2 = []
            counter = 0
        counter += 1
    return liste1


print(splitList([1, 2, 3, 4, 5, 6], 2))
