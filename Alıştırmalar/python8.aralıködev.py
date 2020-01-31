"""
 Hangman oyunu. 1 kafa, 1 govde , 2 kol ve 2 bacak olmak uzere kullanicinin en fazla 6 tane tahmin hakki olabilir.
 Bir listede 1 den baslayarak ardisik numaralarimiz olsun 20 tane, onlardan 10 tane rastgele sayi secelim.
 Kullaniciya tahmin hakki verelim. 6 tahminde, liste icindeki bir rakami bilemezse kaybetsin.
 (bu soruyu while/for/if kullanarak yapin, ikinci bir cevap olarak yine bu soruyu fonksiyon kullanarak yapin)
"""
from random import randint

liste = []

for sayac in range(1, 21):
    liste.append(sayac)

print("liste: " + str(liste))

new_list = []
while len(new_list) <= 10:
    rastgele_sayi = randint(1, len(liste)-1)
    if rastgele_sayi in new_list:
        print("Bu sayı new_list listesi içerisinde var bir daha yazma " + str(rastgele_sayi))
        new_list
    else:
        new_list.append(rastgele_sayi)

print(new_list)
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
