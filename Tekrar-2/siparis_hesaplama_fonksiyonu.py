menu = [
    ["Çay", 1.5],
    ["Kahve", 2.5],
    ["Simit", 1.25],
    ["Sufle", 5],
    ["Pasta Dilimi", 6],
    ["Sütlaç", 5]
]

"""
Bir cafe siparişleri hesaplayan bir program yazmak istiyoruz. Menü fiyatlarda birlikte bir listede tutuluyor
ve biz de siparişleri başka bir liste olarak alıyoruz
Siparişlerin tutarını hesaplayan hesapla fonksiyonunu tamamlayınız.
Kodu çalıştırıp sonucu kontrol ediniz.
"""


def hesapla(siparisler):
    tutar = 0
    for sayi in range(len(siparisler)):
        tutar = tutar + siparisler[sayi] * menu[sayi][1]
    return tutar


print(hesapla([4, 2, 2, 1, 1, 2]))
