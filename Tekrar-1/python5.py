"""
Oyunun yeni özellikleri şöyle olsun:

Oyunda tek şeker vardı. Bunun yerine, biri mavi, diğer sarı iki şeker türü olsun.
Üstelik, bir de kombo özelliği getirelim ki efsane bir oyun olsun.
Her mavi veya sarı şeker 100 puan demek.
Her kombo, 200 puan demek.
Gerekli değişiklikleri yapmak için:

Kullanıcıya kaç mavi ve kaç sarı şeker patlattığını sorun ve mavi_seker ve sari_seker değişkenleri içine alın.
Kullanıcıya kaç kombo yaptığını sorun ve kombo değişkeni içine alın.
Döngü içinde, patlattığı şekerlere ve komboya göre puanını artırın.

Oyunun kuralları:

Oyuncuların seviye atlayabilmesi için en az 1000 puanı alması gerekiyor. Bu puana ulaşana kadar,
 şeker patlatmaya devam etmeli.
Her şeker 100 puan demek.
"""
puan = 0
deneme_sayisi = 1

while puan < 1000:
    mavi_seker = int(input("Kaç mavi şeker patlattın"))
    sari_seker = int(input("Kaç sarı şeker patlattın"))
    kombo = int(input("Kaç kombo şekeri patlattın"))
    puan = puan + (mavi_seker + sari_seker) * 100 + kombo * 200
    deneme_sayisi += 1
    if deneme_sayisi > 3:
        break

print(puan)
if puan >= 1000:
    print("Tebrikler sınır puanının geçtiniz")
else:
    print("Seviye atlayamadınız, tekrar oynamak için 3 gün bekleyin.")
