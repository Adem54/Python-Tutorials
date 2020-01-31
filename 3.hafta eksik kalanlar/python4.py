# Kontrol kodu olarak 123 kullanın:
#
# Kullanıcıya while döngüsü 3 kere doğru pin girme şansı verin. Hatalı girişler için ekrana "Hatalı Giriş.
# Tekrar PIN girin" yazdırın
# 3 girişten birinde doğru pin girilirse "PIN Kabul Edildi. Hesabınıza Erişebilirsiniz." yazdırın.
# 3 girişte de yanlış girilirse "3'den Fazla Giriş Hakkınız Yok. Hesabınız Kilitlendi!" yazdırın


print("ACME Bankası Uygulamasına Hoşgeldiniz.")
giris = input("PIN kodunu girin");

deneme_sayisi = 0
deneme_sayisi = deneme_sayisi + 1

while deneme_sayisi < 3:
    if giris != "123":
        # print("Hatalı Giriş. Tekrar PIN girin")
        giris = input("Hatalı Giriş. Tekrar PIN girin")
    if giris == "123":
        print("PIN Kabul Edildi. Hesabınıza Erişebilirsiniz.")
        break
    deneme_sayisi = deneme_sayisi + 1
    if deneme_sayisi == 3 and giris != "123":
        print("3'den Fazla Giriş Hakkınız Yok. Hesabınız Kilitlendi!")
