ondlalik_sayi=12.34
print(type(ondlalik_sayi))
birinci_sayi = 12
ikinci_sayi = 6
# CTRL ALT L  ile kodları düzenleyebiliriz
bolme = birinci_sayi / ikinci_sayi
print(bolme)
#  / ile işelem yapınca eğer sonuç tam bölünse bile sonuc 2.0  yani float sayı tipinde geri dönüyor buna dikkat edelim
birinci_sayi = birinci_sayi + 12
ikinci_sayi = ikinci_sayi + 1
result = birinci_sayi // ikinci_sayi
print(result)
#  // ama iki tane bölme işlemi yanyana kullanırskak sonuç küsüratlı olsa bile sadece tam sayı kısmını alacaktır
get_remain = birinci_sayi % ikinci_sayi
print("Get remain:" + str(get_remain))
# Bu kodda dikkat ederseniz str içerisine almazsam hata veriyor çünkü string ile integer bir ifadeyi yanyana yazdıramam
# onun için integer ı da str ye çeviriyorum
x = 2
y = 4
x_ussu_y = x ** y
print("x üssü ye: " + str(x_ussu_y))
# VÜCUT KİTLE İNDEKSİ HESAPLAMA
# Beden kitle indeksi, vücut ağırlığının (kg olarak),boy uzunluğunun (metre cinsinden) karesine bölünmesiyle hesaplanır
tall_stature = float(input("Boy uzunluğunuzu ondalık sayı olarak giriniz: "))
# Dikkat edelim float içerisine aldık input u çünkü ondalık bir sayı gireceğiz
body_weight = int(input("Vücut kg ı nızı tam sayı olarak giriniz: "))
body_mass_index = body_weight / (tall_stature * tall_stature)
round_number = round(body_mass_index, 2)
# round(34.24354367,3) dersek virgülden sonra yazdığımız sayı kadar ondalık sayının ondalık kısmını yazar
print("Vücut kitle indexiniz: " + str(round_number))

first_str = "Birinci stringimiz"
second_str = "İkinci stringimiz"
# Concetanation
print(first_str + " " + second_str)

# KENDİ BELİRLEDİĞİMİZ KRİTERE GÖRE ŞİFRE GİRİLEN PROGRAM
# Kriterimiz:Önce 3 tane aynı harf 2 tane de aynı numara karakter girilecek bir şifre olmalı
password_word = input("Bir harf karakteri giriniz")
password_number = input("Bir numara karakteri giriniz")
# succesif concetenation=>  print(3*"abc") abcabcabc
whole_password = 3 * password_word + 2 * password_number
print("Şifreniz: " + whole_password)
print("Şifrenizin uzunluğu: " + str(len(whole_password)))
