"""
Kullanıcıdan alınan 2 basamaklı bir sayının okunuşunu bulan bir fonksiyon yazın.
Örnek: 97 ---------> Doksan Yedi
Not: kullanıcıdan alınan sayı her zaman iki basamaklı olacak
"""

birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayi):
    onlar_basamak = sayi // 10
    birler_basamak = sayi % 10
    okunus = onlar[onlar_basamak] + " " + birler[birler_basamak]
    return okunus


sayi = int(input("Sayı:"))
print(okunus(sayi))
