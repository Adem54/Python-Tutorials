from random import randint


def liste_olustur(baslangic, bitis):
    liste = []
    for sayac in range(baslangic, bitis):
        liste.append(sayac)
    return liste


print(liste_olustur(1, 21))  # içerisine yazacağımız sayılar arasında liste oluşturma fonksiyonu


def diziden_rastgelen_eleman_sec(secilecek_eleman_sayisi, secilecek_liste):
    new_list = []
    sayac = 1
    while sayac <= secilecek_eleman_sayisi:
        random_number = randint(0, len(secilecek_liste))
        eklenen_random_eleman = secilecek_liste[random_number]
        if eklenen_random_eleman in new_list:
            new_list
        else:
            new_list.append(eklenen_random_eleman)

        sayac += 1
    return new_list


# 1 den 20 ye kadar liste oluşturan fonksiyon
liste = liste_olustur(1, 21)
# parametresine verdiğimiz liste içerisinden kaç tane rastgele sayı seçmesini istersek o kadar sayıyı rastgele dizi
# olarak döndüren fonksiyon
diziden_rastgelen_eleman_sec(5, liste)


def tahminle_liste_elemani_bulma(tahmin_sayisi):
    liste = liste_olustur(1, 21)
    rastgele_secilen_liste = diziden_rastgelen_eleman_sec(10, liste)
    print(rastgele_secilen_liste)
    sayac = 1
    while sayac <= tahmin_sayisi:
        tahmin_edilen_sayi = int(input("Bir sayı tahmin ediniz?"))

        if tahmin_edilen_sayi in rastgele_secilen_liste:
            print(str(sayac) + ". tahminde rastgele_secilen_liste içerisindeki bir rakamı buldunuz ")
            break
        else:
            print(str(sayac) + ". tahminde rastgele_secilen_liste içerisindeki bir rakamı bulamadınız lütfen yeniden "
                               "bir sayı tahmin edin ")

        sayac += 1


tahminle_liste_elemani_bulma(4)
"""
tahmin_sayisi = 1
while tahmin_sayisi <= 6:
    tahmin_edilen_sayi = int(input("Bir sayı tahmin ediniz?"))
    if tahmin_edilen_sayi in new_list:
        print(str(tahmin_sayisi) + ". tahminde newlist içerisindeki bir rakamı buldunuz ")
        break
    else:
        print(str(tahmin_sayisi) + ". tahminde newlist içerisindeki bir rakamı bulamadınız lütfen yeniden bir"
                                   " sayı tahmin edin ")
    tahmin_sayisi += 1

print(liste)

"""
