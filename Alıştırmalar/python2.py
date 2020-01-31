# SORU-2
# Ilk 2 terimi 3 ve 4 olan asagidaki kurala gore olusturulacak sayi dizisinin ilk 15 terimini ekrana yazacak python
# programini while dongusu kullanarak yaziniz.
#
# Dizinin her teriminin kendinden onceki son 2 terimin toplami seklinde olusmasi gerekiyor yani su sekilde;
# Dizimizin ilk 2 terimi bize verilmisti zaten 3 ve 4.
# 3. terimimiz  yukaridaki sarta gore 1. ve 2. terimin toplami olmasi gerekiyor yani 3 + 4 = 7
#
#
# 3 4 7
# 4. terimimizin de 2. ve 3. terimin toplami olmasi gerekiyor; yani 4 + 7 = 11
# 3 4 7 11
# 5. terimimiz de 3. ve 4. terimin toplami olmali; yani 7 + 11 = 18
# 3 4 7 11 18
# 6. terimimiz de 4. ve 5. terimin toplami olmali; yani 11 + 18 = 29
# 3 4 7 11 18 29
# Seri bu sekilde devam etmeli
#
#
# Ornek program outputu
# Serinin ilk 15 terimi =  3 4 7 11 18 29 47 76 123 199 322 521 843 1364 2207
#
# Serideki sayilari alt alta yazdirmanizda bir problem yok, ancak  daha okunakli olmasi icin sayilari yan yana
# ayni satirda yazdirmak isterseniz Soru-1'deki print() ozelligini kullanabilirsiniz.
# =====================================================================================================================
# Dizinin her teriminin kendinden onceki son 2 terimin toplami seklinde olusmasi gerekiyor yani su sekilde;
# Dizimizin ilk 2 terimi bize verilmisti zaten 3 ve 4.
# 3. terimimiz  yukaridaki sarta gore 1. ve 2. terimin toplami olmasi gerekiyor yani 3 + 4 = 7

list = [3, 4]
print(list[len(list) - 1] + list[len(list) - 2])
list_length=len(list)
while list_length < 15:
    list.append(list[list_length - 1] + list[list_length - 2])
    list_length = len(list)
print(list)
