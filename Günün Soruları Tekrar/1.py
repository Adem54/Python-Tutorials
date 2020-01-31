"""
Ekteki daha once soru cozum derslerinde de kullandigimiz, asal_mi fonksiyonunu kullanarak
ortak_asallar(liste1, liste2) fonksiyonunu yaziniz.
ortak_asallar fonksiyonu su sekilde calismali, 2 tane tam sayi iceren listeyi parametre olarak alip
bu listelerdeki asal sayilarin ortak olanlarini baska bir listeye ekleyip
olusan bu listeyi geri donmek.
"""


def asal_mi(sayi):
    is_Asal = False
    counter = 2
    if sayi == 2:
        is_Asal = True
    while counter < sayi:
        if sayi % counter == 0:
            is_Asal = False
            break
        else:
            is_Asal = True

        counter += 1
    if is_Asal:
        return sayi


print(asal_mi(43))


def ortak_asallar(liste1, liste2):
    ortak_asal = []
    for eleman in liste1:
        if eleman in liste2:
            result = asal_mi(eleman)
            if result is not None:
                ortak_asal.append(eleman)
    return ortak_asal

# Bir veri için boş değilse diye sorgulatacaksak şu şekilde sorugaltabiliriz
# value is not None dersek o zaman bu değer boş değilse böyle yaz demiş oluruz...
liste11 = [3, 5, 7, 9, 11, 13, 14, 15,17]
liste12 = [2, 3, 5, 7, 11, 15,17]
print(ortak_asallar(liste11, liste12))
