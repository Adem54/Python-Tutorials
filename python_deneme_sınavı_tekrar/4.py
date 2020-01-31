"""
Peynirin kilosunun 30TL , Zeytinin kilosunun 20TL oldugu bir dukkan icin ,
kullanicidan kac kilo peynir , kac kilo zeytin alacagi bilgisini girdi olarak alip,
odenmesi gerek toplam fiyati ekrana yazdiran python programini yaziniz.

Ornek Program Outputu
kac kilo peynir istiyorsunuz: 2
kac kilo zeytin istiyorsunuz: 2
Toplam Fiyat =  100TL
"""
peynir_miktar = int(input("Kaç kg peynir alınacak"))
zeytin_miktar = int(input("Kaç kg zeytin alınacak"))
odenecek_miktar = peynir_miktar * 30 + zeytin_miktar * 20
print(odenecek_miktar)
