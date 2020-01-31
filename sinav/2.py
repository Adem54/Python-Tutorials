"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve
şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(metre) *  Boy(metre)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""
boy = float(input("Metre cinsinden boyunuzu giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))
beden_kitle_indeks = kilo / (boy * boy)
if beden_kitle_indeks < 18.5:
    print("Zayıf")
elif 18.5 <= beden_kitle_indeks < 25:
    print("Normal")
elif 25 <= beden_kitle_indeks < 30:
    print("Fazla Kilolu")
else:
    print("Obez")
