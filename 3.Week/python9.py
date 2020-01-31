# Kullanıcıya while döngüsü 3 kere doğru pin girme şansı verin.Hatalı girişler için ekrana "Hatalı Giriş.
# Tekrar PIN girin" yazdırın
# 3 girişten birinde doğru pin girilirse "PIN Kabul Edildi. Hesabınıza Erişebilirsiniz." yazdırın.
# 3 girişte de yanlış girilirse "3'den Fazla Giriş Hakkınız Yok. Hesabınız Kilitlendi!" yazdırın
print("ACME Bankası Uygulamasına Hoşgeldiniz.")
deneme_sayisi = 0
pin_kodu = 1234
giris = input("PIN kodunu girin")
deneme_sayisi = deneme_sayisi + 1

while deneme_sayisi < 3:
    if giris != "1234":
        print("Hatalı Giriş. Tekrar PIN girin")
        giris = input("PIN kodunu girin")
        deneme_sayisi = deneme_sayisi + 1
    elif giris == "1234":
        print("PIN Kabul Edildi. Hesabınıza Erişebilirsiniz.")
        break  # Eğer kodu girince orda artık sayacı durdurmasını istersek o zaman doğrdudan break kodunu kullanırız
        # ya da biz sayacı bitirmek için koşulu false yapacak birşey yapmalıyız o da belki koşul etkileyen değişken
        # koşula girmeyecek sayıya eşitleyebiliriz
    if deneme_sayisi == 3 and giris != "1234":
        print("3'den Fazla Giriş Hakkınız Yok. Hesabınız Kilitlendi!")
