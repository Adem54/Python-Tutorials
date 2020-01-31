# Deneme

veri_tabaninda_kayitli_sifre = 'abc'

kullanicinin_girdigi_sifre = input('Hesabınıza Giriş İçin Şifre Girin Lütfen')

deneme_sayisi = 1
while veri_tabaninda_kayitli_sifre != kullanicinin_girdigi_sifre and deneme_sayisi < 3:
    kullanicinin_girdigi_sifre = input('Yanlış girdiniz. Tekrar deneyin:')
    deneme_sayisi = deneme_sayisi + 1

print("deneme_sayisi=" + str(deneme_sayisi))
if deneme_sayisi >= 3:
    print("Hesabı kilitliyorum")
else:
    print('Hoşgeldiniz, banka hesabınızı kullanabilirsiniz')
