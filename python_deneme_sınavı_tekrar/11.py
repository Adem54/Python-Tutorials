"""
Soru 1- Elimizde magazamizda satilan urunler ve fiyatlarinin tutuldugu su formatta bir listemiz var
urun_fiyat_listesi = [["canta", 50], ["ayakkabi", 65], ["ceket", 100]]
listedeki urunlerin fiyat listesini alacagi parametredeki zam miktarina gore guncelleyip
yeni bir urun fiyat listesi seklinde geri donen
fiyat_guncelleme(liste, zam) fonksiyonunu yaziniz
liste: fiyat listesi , ornek [["canta", 50], ["ayakkabi", 65], ["ceket", 100]]
zam: ornegin zam 10 liraysa fiyatlar 10 lira artirilmali ve fonksiyondan dönen liste aşağıdaki gibi olmalı
[["canta", 60], ["ayakkabi", 75], ["ceket", 110]]
"""

# Şunu hiçbirzamaan unutmamalıyız ki eğer bir liste içerisinde o listeyi değiştirmeden eleman değiştireceksek o zaman
#yapacağımız iş şudur ki o elemanın indisini liste[indis] yazıp  yazmak istediğmiz yeni değeri yazmalıyız ki o liste
#içinde değişiklik yapabilelim
def fiyat_guncelleme(liste, zam):
    for urun in liste:
        urun[1] += zam
    return liste


urun_fiyat_listesi = [["canta", 50], ["ayakkabi", 65], ["ceket", 100]]
listem = fiyat_guncelleme(urun_fiyat_listesi, 20)
print(listem)
