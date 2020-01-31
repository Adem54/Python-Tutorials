"""
Ekteki daha once soru cozum derslerinde de kullandigimiz, asal_mi fonksiyonunu kullanarak
ortak_asallar(liste1, liste2) fonksiyonunu yaziniz.
ortak_asallar fonksiyonu su sekilde calismali, 2 tane tam sayi iceren listeyi parametre olarak alip
bu listelerdeki asal sayilarin ortak olanlarini baska bir listeye ekleyip
olusan bu listeyi geri donmek.
Hatirlatma
asal_mi(sayi) bir tam sayi alip eger bu sayi asalsa True, degilse False donen bir fonksiyon.
Fonksiyonunuzu su 2 listede test edebilirsiniz.
liste1 = [2, 3 ,4, 20, 23 , 58 , 92, 107 ]
liste2 = [3 ,6, 8, 11, 97, 102, 107]
fonsiyonumuz geriye soyle bir liste donmeli
[3, 107]
"""


def ortak_asallar(liste1, liste2):
    liste3 = []
    for eleman in liste1:
        if eleman in liste2:
            print(eleman)
            is_asal = False
            sayac = 2
            if eleman == 2:
                is_asal=True
            while sayac < eleman:
                if eleman % sayac == 0:
                    is_asal=False
                    break
                else:
                    is_asal=True
                    sayac+=1

            if is_asal:
                liste3.append(eleman)


    return liste3


liste1 = [2, 3, 4, 11, 20, 23, 58, 92, 107]
liste2 = [2,3, 6, 8, 11, 23, 97, 102, 107]
print(ortak_asallar(liste1, liste2))
