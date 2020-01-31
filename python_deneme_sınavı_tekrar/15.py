"""
Bir ogretmenin sinifindaki ogrencilerin isimleri ve notlarini  input olarak alan
ve bu bilgiyi asagidaki formatta verildigi sekilde not_listesi degiskeninde tutan python programini yaziniz.
Program ogretmen ogrenci adi olarak "xxx" girene kadar devam etmeli ,
ogretmen isim olarak "xxx" girdiginde, program not_listesi'ni ekrana yazdirip sonlanmali.
not_listesi = [['Ayse', 95], ['Ali', 85]]
Ornek Program Outputu
=====================================
Ogrenci Adi: Ayse
Ayse'nin notunu giriniz: 95
Ogrenci Adi: Ali
Ali'nin notunu giriniz: 85
Ogrenci Adi: xxx
[['Ayse', 95], ['Ali', 85]]
======================================
"""
ogrenci_adi = ""
ogrenci_notu = 0
not_listesi = []
while ogrenci_notu != "xxx":
    ogrenci = []
    ogrenci_adi = input("Öğrenci adı giriniz")
    if ogrenci_adi == "xxx":
        print(not_listesi)
        break
    ogrenci_notu = int(input("Öğrenci notu giriniz"))
    ogrenci.append(ogrenci_adi)
    ogrenci.append(ogrenci_notu)
    not_listesi.append(ogrenci)


