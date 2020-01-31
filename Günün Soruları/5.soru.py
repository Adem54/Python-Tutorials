"""
[['ocak', -5, 2, 2, -3, 4, 0, 5, 1, 4, 1, -3, 2, -1, 4, 1, 5, 4, -1, 5, -5, -5, -3, -2, 4, 2, -2, -3, 2, 5, 0, -4],
['subat', -7, -1, 2, -2, 3, -6, 0, 2, 2, -7, -4, -1, 1, 1, 0, -1, -4, -3, 1, -2, 1, -2, -7, -6, -2, 3, 0, -7],
['mart', 3, 3, 7, 4, 0, 1, 7, 5, -1, 0, 7, 5, 0, 3, 1, 4, 4, 4, -1, 0, 0, 3, 0, 5, 5, 1, 1, 0, 4, 2, 6],
['nisan', 2, 11, 12, 10, 10, 9, 10, 4, 12, 12, 5, 3, 12, 2, 4, 8, 7, 9, 10, 4, 3, 7, 2, 9, 8, 7, 2, 13, 4, 15],
['mayis', 16, 17, 14, 9, 7, 7, 9, 10, 19, 16, 5, 9, 17, 14, 10, 17, 16, 10, 16, 11, 6, 18, 19, 5, 19, 20, 13,
17, 8, 21, 6],
['haziran', 24, 18, 25, 18, 20, 24, 25, 17, 21, 20, 24, 20, 21, 22, 25, 22, 24, 20, 22, 21, 23,
21, 24, 20, 23, 25, 17, 21, 21, 20],
['temmuz', 35, 34, 37, 33, 36, 39, 29, 30, 38, 34, 36, 40, 37, 36, 33, 34,
 31, 33, 35, 36, 29, 39, 36, 27, 34, 31, 27, 28, 39, 33, 35],
['agustos', 35, 33, 32, 30, 29, 32, 30, 30, 32,
  26, 26, 31, 28, 28, 34, 25, 26, 30, 33, 35, 25, 28, 30, 28, 34, 30, 32, 34, 26, 34, 27],
['eylul', 17, 20,
  20, 24, 17, 15, 19, 21, 20, 24, 15, 18, 17, 15, 25, 19, 15, 22, 21, 24, 21, 15, 21, 24, 15, 15, 22, 22, 20, 19],
['ekim', 17, 16, 17, 20, 11, 12, 10, 15, 14, 20, 20, 19, 10, 16, 17, 12, 17, 19, 14, 13, 18, 16, 13, 17, 13,
    12, 14, 11, 16, 16, 16],
['kasim', 7, 6, 4, 10, 9, 4, 4, 8, 5, 5, 5, 6, 9, 10, 9, 9, 5, 9, 3, 4, 7, 10, 4,
    8, 3, 7, 8, 10, 6, 3],
['aralik', 0, 2, -1, 3, 1, 1, 6, 2, 3, -1, 8, 6, 5, 1, 7, 8, 0, 1, -1, 5, 0, -1,
     3, 1, 6, 7, 8, 2, 6, 5, 5]]



Verilen ekteki yillik_sicaklik_verisi bilgisine gore:
1- Her ayin ortalama sicakligini
2- Yillin sicaklik ortalamasi en yuksek ayini
3- Yilin sicaklik ortalamasi en dusuk ayini
4- Yilin en sicak gun ya da gunlerini
5  Yilin en soguk gun ya da gunlerini ekrana yazdiran  python programini yaziniz.
"""

sicaklik_verileri = [
    ['ocak', -5, 2, 2, -3, 4, 0, 5, 1, 4, 1, -3, 2, -1, 4, 1, 5, 4, -1, 5, -5, -5, -3, -2, 4, 2, -2, -3, 2, 5, 0, -4],
    ['subat', -7, -1, 2, -2, 3, -6, 0, 2, 2, -7, -4, -1, 1, 1, 0, -1, -4, -3, 1, -2, 1, -2, -7, -6, -2, 3, 0, -7],
    ['mart', 3, 3, 7, 4, 0, 1, 7, 5, -1, 0, 7, 5, 0, 3, 1, 4, 4, 4, -1, 0, 0, 3, 0, 5, 5, 1, 1, 0, 4, 2, 6],
    ['nisan', 2, 11, 12, 10, 10, 9, 10, 4, 12, 12, 5, 3, 12, 2, 4, 8, 7, 9, 10, 4, 3, 7, 2, 9, 8, 7, 2, 13, 4, 15],
    ['mayis', 16, 17, 14, 9, 7, 7, 9, 10, 19, 16, 5, 9, 17, 14, 10, 17, 16, 10, 16, 11, 6, 18, 19, 5, 19, 20, 13,
     17, 8, 21, 6],
    ['haziran', 24, 18, 25, 18, 20, 24, 25, 17, 21, 20, 24, 20, 21, 22, 25, 22, 24, 20, 22, 21, 23,
     21, 24, 20, 23, 25, 17, 21, 21, 20],
    ['temmuz', 35, 34, 37, 33, 36, 39, 29, 30, 38, 34, 36, 40, 37, 36, 33, 34,
     31, 33, 35, 36, 29, 39, 36, 27, 34, 31, 27, 28, 39, 33, 35],
    ['agustos', 35, 33, 32, 30, 29, 32, 30, 30, 32,
     26, 26, 31, 28, 28, 34, 25, 26, 30, 33, 35, 25, 28, 30, 28, 34, 30, 32, 34, 26, 34, 27],
    ['eylul', 17, 20,
     20, 24, 17, 15, 19, 21, 20, 24, 15, 18, 17, 15, 25, 19, 15, 22, 21, 24, 21, 15, 21, 24, 15, 15, 22, 22, 20, 19],
    ['ekim', 17, 16, 17, 20, 11, 12, 10, 15, 14, 20, 20, 19, 10, 16, 17, 12, 17, 19, 14, 13, 18, 16, 13, 17, 13,
     12, 14, 11, 16, 16, 16],
    ['kasim', 7, 6, 4, 10, 9, 4, 4, 8, 5, 5, 5, 6, 9, 10, 9, 9, 5, 9, 3, 4, 7, 10, 4,
     8, 3, 7, 8, 10, 6, 3],
    ['aralik', 0, 2, -1, 3, 1, 1, 6, 2, 3, -1, 8, 6, 5, 1, 7, 8, 0, 1, -1, 5, 0, -1,
     3, 1, 6, 7, 8, 2, 6, 5, 5]]
"""
Verilen ekteki yillik_sicaklik_verisi bilgisine gore:
1- Her ayin ortalama sicakligini
2- Yillin sicaklik ortalamasi en yuksek ayini
3- Yilin sicaklik ortalamasi en dusuk ayini
4- Yilin en sicak gun ya da gunlerini
5  Yilin en soguk gun ya da gunlerini ekrana yazdiran  python programini yaziniz.
"""
# 1)
toplam_liste = []
for ay_sicaklik_verileri in sicaklik_verileri:
    toplam = 0
    ortalama = 0
    liste = []
    for sayi in range(len(ay_sicaklik_verileri)):
        ay = ay_sicaklik_verileri[0]
        if sayi > 0:
            toplam = toplam + ay_sicaklik_verileri[sayi]
    ortalama = round((toplam / sayi), 2)
    liste.append(ay)
    liste.append(ortalama)
    toplam_liste.append(liste)

print(liste)
print(toplam_liste)  # toplam liste tüm aylar ve sıcaklik ortalamalarının olduğu listeler listesidir

# 2
max_sicaklik = 0
min_sicaklik = 0
for eleman in toplam_liste:

    sayac = 0
    ort_sicaklik = 0
    for elem in eleman:
        sayac += 1

        if max_sicaklik < eleman[1]:
            max_sicaklik = eleman[1]
        if min_sicaklik > eleman[1]:
            min_sicaklik = eleman[1]
print(max_sicaklik)
print(min_sicaklik)

max_sicaklik = 0
min_sicaklik = 0

for ay_sicaklik_verileri in sicaklik_verileri:
    max_sicklik_list = []
    min_sicaklik_list = []

    for gunluk_sicaklik in ay_sicaklik_verileri:
        if type(gunluk_sicaklik) != str:
            if max_sicaklik < gunluk_sicaklik:
                max_sicaklik = gunluk_sicaklik
            if min_sicaklik > gunluk_sicaklik:
                min_sicaklik = gunluk_sicaklik
    max_sicklik_list.append(max_sicaklik)
    min_sicaklik_list.append(min_sicaklik)

print("max-sicaklik: " + str(max_sicklik_list))
print("min-sicaklik:" + str(min_sicaklik_list))

# Son olarak her ayin en büyük ve en küçük sicaklik derecesini ay adi ile birlikte bir liste içerisine yazdıralım
tum_aylar_max_min_sicaklik = []
for ay_sicaklik_verileri in sicaklik_verileri:
    ay_max_min_sicaklik = []
    max_sicaklik = -100
    min_sicaklik = 100
    ay_adi = ""
    for gunluk_sicaklik in ay_sicaklik_verileri:
        if type(gunluk_sicaklik) != str:
            if max_sicaklik < gunluk_sicaklik:
                max_sicaklik = gunluk_sicaklik
            if min_sicaklik > gunluk_sicaklik:
                min_sicaklik = gunluk_sicaklik
        else:
            ay_adi = gunluk_sicaklik
    ay_max_min_sicaklik.append(ay_adi)
    ay_max_min_sicaklik.append(max_sicaklik)
    ay_max_min_sicaklik.append(min_sicaklik)
    tum_aylar_max_min_sicaklik.append(ay_max_min_sicaklik)

print(tum_aylar_max_min_sicaklik)

"""

Bu bir eksiklik :
Ağabey max_sicaklik=0  dedikten sonra     max_sicaklik < for içinde dönen değerden diye yazdığımızda ve eğer 
bu değer doğru ise  max_sicaklik=for içinden gelen değer diyorduk ya burda bir açık var o açık şu ki eğer for 
içindeki değerlerden bir tanesi bile max_sicaklik <  şartına uyuyorsa yani liste içindeki değerlerden en az bir 
tanesi bile max_sicakliktan büyükse sorun yok ancak eğer liste içindeki değerlerden hiçbirisi
max_sicaklik< liste içindeki değer  şartına uymazsa tamamı da max_sicakliktan küçükse o zaman bizim bu olay
patlar ve max_sicaklik ilk atadığımız değer olarak 0 olarak  kalır ve liste içindeki en büyük değri bulamaz onun 
için şunu yapmalıyız eğer max_sicaklik buluyorsak max_sicakliğin ilk değerini bulacağımız liste içindeki değerlerden
en az bir tanesinden daha küçük vermeliyiz aynı mantıkla da min_sicaklik bulurken de min_sicaklik değerini 
ise liste içindeki değerlerden en az bir tanesinden daha büyük bir değer vermeliyiz ilk değer olarak min_sicakliği


[['ocak', 5, -5], ['subat', 3, -7], ['mart', 7, -1], ['nisan', 15, 0], ['mayis', 21, 0], ['haziran', 25, 0], 
['temmuz', 40, 0], ['agustos', 35, 0], ['eylul', 25, 0], ['ekim', 20, 0], ['kasim', 10, 0], ['aralik', 8, -1]]
"""
