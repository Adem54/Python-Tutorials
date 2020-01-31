# Bir cafe siparişleri hesaplayan bir program yazmak istiyoruz. Menü fiyatlarda birlikte bir listede tutuluyor ve
# biz de siparişleri başka bir liste olarak alıyoruz
# Siparişlerin tutarını hesaplayan hesapla fonksiyonunu tamamlayınız.
# Kodu çalıştırıp sonucu kontrol ediniz.

menu = [
    ["Çay", 1.5],
    ["Kahve", 2.5],
    ["Simit", 1.25],
    ["Sufle", 5],
    ["Pasta Dilimi", 6],
    ["Sütlaç", 5]
]
# print(hesapla([4, 2, 2, 1, 1, 2]))

def hesapla(siparisler):
    tutar = 0
    for sayi in range(len(menu)):
        for adet in range(len(siparisler)):
            if sayi == adet:
                tutar = tutar + siparisler[adet] * menu[sayi][1]

    return tutar


print(hesapla([4, 2, 2, 1, 1, 2]))
print(hesapla([2, 2, 2, 2, 2, 2]))

