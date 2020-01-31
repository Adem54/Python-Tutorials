"""
Öğretmeni Barry'den, elindeki iki sayıdan en fazla asal sayı böleni olan sayıyı bulmasını istiyor.
Barry'nin yazmak istediği;
  en_fazla_asal_sayi_bolenliyi_bul(sayi1, sayi2) fonksiyonunu yazınız.

Bu fonksiyonu yazarken size hazır olarak verilen asal_mi() fonksiyonundan yararlanabilirsiniz.
  Bu fonksiyon bir sayının asal sayı olup olmadığını bize söylüyor.
  Eğer sayı, asal sayı ise True, değilse False cevabı veriyor.

Örnek:
Input: en_fazla_asal_sayi_bolenliyi_bul(6, 11)
Output: 6
Açıklama:
  6 yı bölen asal sayılar 2 ve 3 -> 2 adet
  11 i bölen asal sayılar 11 -> 1 adet

Input: en_fazla_asal_sayi_bolenliyi_bul(18, 70)
Output: 70
Açıklama:
  18 i bölen asal sayılar 2 ve 3 -> 2 adet
  70 i bölen asal sayılar 2, 5 ve 7 -> 3 adet

Not: Eşit sayıda asal bölenli olması durumunu gözardı edebilirsiniz.
"""


def asal_mi(sayi):
    # Eger sayi 2 ise True
    if sayi == 2:
        return True
    # Eger sayi 2 den kucukse False
    elif sayi < 2:
        return False
    # Diger durumlarda
    else:
        # 2 den baslayarak sayiya kadar olan tum sayilar icin
        for i in range(2, sayi):
            # Eger tam bolunurse False
            if sayi % i == 0:
                return False
        # True
        return True


def en_fazla_asal_sayi_boleni_bul(sayi1, sayi2):
    liste1 = []
    liste2 = []
    for sayi11 in range(sayi1 + 1):
        if sayi11 > 1:
            if sayi1 % sayi11 == 0 and asal_mi(sayi11):
                liste1.append(sayi11)

    for sayi12 in range(sayi2 + 1):
        if sayi12 > 1:
            if sayi2 % sayi12 == 0 and asal_mi(sayi12):
                liste2.append(sayi12)

    liste1_uzunluk = len(liste1)
    liste2_uzunluk = len(liste2)
    print("liste1:" + str(liste1))
    print("liste2: " + str(liste2))
    if liste1_uzunluk >= liste2_uzunluk:
        return sayi1
    if liste1_uzunluk < liste2_uzunluk:
        return sayi2


sayi111 = int(input("sayi1? "))
sayi222 = int(input("sayi2? "))

print(en_fazla_asal_sayi_boleni_bul(sayi111, sayi222))
