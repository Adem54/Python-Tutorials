"""
Bir ogretmenin sinifindaki ogrencilerin isimleri ve notlarini  input olarak alan
ve bu bilgiyi asagidaki formatta verildigi sekilde not_listesi degiskeninde tutan python programini yaziniz.

Program ogretmen ogrenci adi olarak "xxx" girene kadar devam etmeli , ogretmen isim olarak
 "xxx" girdiginde, program not_listesi'ni ekrana yazdirip sonlanmali.

not_listesi = [['Ayse', 95], ['Ali', 85]]

Ornek Program Outputu
=====================================
Ogrenci Adi: Ayse
Ayse'nin notunu giriniz: 95
Ogrenci Adi: Ali
Ali'nin notunu giriniz: 85
Ogrenci Adi: xxx
[['Ayse', 95], ['Ali', 85]]
"""
# Eğer ogrenci değişkenini dışada tanımlasa idik listeler mutable olduğu için en son ogrenci listesinin elemanları
# ne ise ilk döngüde not_listesi içerisine kaydedilen ogrenci listesi de en son kaydedilen ogrenci listesi ile aynı
# elemanlara sahip olmuş olacak çünkü mutable değişebilen verilerdir referans türü veriler


ogrenci_adi = ""

not_listesi = []

while ogrenci_adi != "xxx":
    ogrenci = []
    ogrenci_adi = input("Ogrenci Adi: ")
    if ogrenci_adi == "xxx":
        break
    ogrenci_notu = int(input(str(ogrenci_adi) + "'nin notunu giriniz:"))
    ogrenci.append(ogrenci_adi)
    ogrenci.append(ogrenci_notu)
    not_listesi.append(ogrenci)

print(not_listesi)
