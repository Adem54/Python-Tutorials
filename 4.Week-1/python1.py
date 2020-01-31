# Üs alma veya kuvvetini bulma
print(2 ** 4)
print(16 ** 0.5)  # karekökünü bu şekilde bulunabilir

print(17 % 4)
print(-17 % 4)  # sonuç 3 verir şu şekilde biz -17 den küçük olan en büyük 4 ile bölünebilen negatif sayıya bakarız
# o da -3 tür -20 olabilmesi için ancak burda python onun pozitifini alır ve +3 verir cevabı
print(-13 % 3)  # burda da -13 ten daha küçük 3 e bölünebilen en büyük sayı -15 tir ve onun içinde -2 ye ihtiyacımız var
# ancak python bize -2 nin pozitifi olan +2 yi verecektir
print(9 / 4)
print(9 // 4)
print("-----------------------------------------------------")

# Mutlak değeri bulan programı yazalım
sayi = int(input("Bir sayı giriniz?"))

if sayi < 0:
    print(-(sayi))
else:
    print(sayi)

print("-----------------------------------------------------")

# Kullanıcıdan alınan iki sayının mutlak değerlerinin toplamını bulan programa ihtiyacımız olsun.
# Örneğin kullanıcı, -2 ve 5 girerse ekran, 7 yazsın, veya 1, -3 girerse 4 yazsın.
sayi1 = int(input("Birinci sayıyı giriniz"))
sayi2 = int(input("İkinci sayıyı giriniz"))

if sayi1 < 0 and sayi2 > 0:
    print(sayi2 + (-1 * sayi1))
elif sayi1 < 0 and sayi2 < 0:
    print(-1 * sayi1 + -1 * sayi2)
elif sayi1 > 0 and sayi2 < 0:
    print(sayi1 + (-1 * sayi2))
elif sayi1 > 0 and sayi2 > 0:
    print(sayi1 + sayi2)
