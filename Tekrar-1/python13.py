"""
Çalıştığımız bankanın cep telefonu uygulamasını geliştiriyoruz. Uygulamanın girişinde PIN kodu sorup,
3 kere yanlış girilirse uygulamayı tamamen kapatacağız.

Kontrol kodu olarak 123 kullanın:

Kullanıcıya while döngüsü 3 kere doğru pin girme şansı verin. Hatalı girişler için ekrana
 "Hatalı Giriş. Tekrar PIN girin" yazdırın
3 girişten birinde doğru pin girilirse "PIN Kabul Edildi. Hesabınıza Erişebilirsiniz." yazdırın.
3 girişte de yanlış girilirse "3'den Fazla Giriş Hakkınız Yok. Hesabınız Kilitlendi!" yazdırın
"""

sifre = 123

sayac = 1

while sayac <= 3:
    denenen_sifre = int(input("Lütfen şifrenizi girin"))
    if denenen_sifre == sifre:
        print("PIN Kabul Edildi. Hesabınıza Erişebilirsiniz.")
        break
    else:
        print("Hatalı Giriş. Tekrar PIN girin")
    if sayac == 3:
        print("3'den Fazla Giriş Hakkınız Yok. Hesabınız Kilitlendi!")
    sayac += 1
