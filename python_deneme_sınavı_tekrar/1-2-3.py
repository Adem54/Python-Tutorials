"""
Kullanicinin girdigi  pozitif tam sayi'yi x degiskeninde, ayni sayi'nin  2 katini y degiskeninde tutan
ve y degiskenini ekrana yazdiran python programini yaziniz.
"""
x = int(input("Bir sayı giriniz"))
y = 2 * x
print(y)

"""
Kullanicidan pozitif bir sayi alan ve kullanicinin girdigi sayinin 7'ye bolumunden kalani 
ekrana yazdiran python programini yaziniz.
"""
a = int(input("Bir sayı giriniz"))
kalan = a % 7
print(kalan)

ad = input("Adı gir")
soyad = input("Soyad gir")
print(soyad + " " + ad)
