"""
Öğrencilerin dersi geçebilme şartını yazmak istiyoruz.

Öğrenci, 5 'ten az ders alıyorsa ve hiç bir dersten kalmamış ise sınıfı geçebilmesini istiyoruz.
Bu koşulu sağlayan if koşulunu soru işareti yerine yazın.
"""

alinan_ders_sayisi = int(input("Kaç ders aldınız?"))
kalinan_ders_sayisi = int(input("Kaç dersten kaldınız?"))

if alinan_ders_sayisi < 5 and kalinan_ders_sayisi == 0 :
    print("Dersten geçtin")
elif 5 <= alinan_ders_sayisi <= 8  and kalinan_ders_sayisi <= 1:

else:
    print("Dersten kaldın")
"""
"Aldığı ders sayısı 5-8 arasında(5 ve 8 dahil) ise, sınıfı geçebilmesi için en fazla 1 dersten kalması gerekir" 
koşulunu soru işareti yerine yazın.
"""
