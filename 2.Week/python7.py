# Güzel haber: şeker patlatma oyunumuzun ilk versiyonu yeterince ilgi çekti. Ama oyuncular sıkılıp bırakmaya başladılar.
# Oyuna yeni özellikler ekleyip, sıkılmalarını engellememiz lazım.

# Oyunun yeni özellikleri şöyle olsun:

# Oyunda tek şeker vardı. Bunun yerine, biri mavi, diğer sarı iki şeker türü olsun.
# Üstelik, bir de kombo özelliği getirelim ki efsane bir oyun olsun.
# Her mavi veya sarı şeker 100 puan demek.
# Her kombo, 200 puan demek.
# Yeni özellik olarak "deneme sayısı sınırı" ekleyelim. 3 defa deneyerek yeterli puana erişemezse,
# oyun sona erecek şekilde kodumuzu değiştirelim:
puan = 0

while puan < 1000:
    deneme_sayisi_siniri = 0
    mavi_seker = int(input("Bu turda kaç mavi şeker patlattın?"))
    deneme_sayisi_siniri = deneme_sayisi_siniri + 1
    sari_seker = int(input("Bu turda kaç sarı şeker patlattın?"))
    deneme_sayisi_siniri = deneme_sayisi_siniri + 1
    kombo = int(input("Bu turda kaç kombo yaptın?"))
    deneme_sayisi_siniri = deneme_sayisi_siniri + 1

    puan = puan + mavi_seker * 100
    puan = puan + sari_seker * 100
    puan = puan + kombo * 200

    if deneme_sayisi_siniri <= 3 and puan < 1000:
        print("Oyununuz malesef " + str(puan) + " puan ile sona ermiştir")
    else:
        print("Tebrikler " + str(puan) + " puan alarak oyunu başarı ile tamamladınız")
