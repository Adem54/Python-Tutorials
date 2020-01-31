# Kullanıcın verdiği sayılar arasından en küçüğünü bulan bir program yazmak istiyoruz.
# Bu program, kullanıcıdan rakam girmesini isteyecek ve bu işlem kullanıcı sıfır girene kadar devam edecek.
# Kullanıcı sıfır girdiğinde, o ana kadar girilmiş olan sayılardan en küçük olanı gösterecek.

girilen_sayi = int(input("Bir sayi giriniz: "))
en_kucuk_sayi = girilen_sayi
while girilen_sayi > 0:
    # Önce if koşulunu yazıp sonra tekrar sayı girin demeliyiz çünkü yukardan gelen sayıyı
    # koşula tabi tutmalıyız onu koşula tabi tutmadan tekrar bir sayı istersek eğer o gelen
    # sayı en küçük olacaksa onu anlayamayız ve gözden kaçırmıış oluruz ve bu şekilde en küçük
    # sayıyı bulamayız
    if 0 < girilen_sayi < en_kucuk_sayi:
        en_kucuk_sayi = girilen_sayi
    girilen_sayi = int(input("Tekar bir sayi giriniz: "))


print("Şu ana kadar girilen en küçük sayı: " + str(en_kucuk_sayi))
