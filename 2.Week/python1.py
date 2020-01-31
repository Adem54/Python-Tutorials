# Dikkat edelim burda True ve False değerlerini baş harfleri büyük  yazılmış...
# Unutmayalım kodlarımız sola dayalı olmalı boşluk olmamalı bu python da önemlidir
bool_true = True
bool_false = False
first_number = 4
second_number = 5
# Karşılaştırma İşlemini Doğrudan Değişkene Atamak!!!
result = first_number >= second_number
print("result:  " + str(result))
katilmak_isteyenler = "Evet"
desicion = katilmak_isteyenler == "Evet"
print("desicion:  " + str(desicion))

# Python da if bloğu ile çalışmak
# if ifadesi ve koşuldan sonraki koşul gerçekleşmesi durumunda yazılacak statement lar yani kod cümleleri indentation
# yani girintili olmalıdırlar ve aynı hizada olmalıdırlarki if bloğu içerisinde olduğunu python anlasın ve
# ona göre işlem yapsın
# Şifre Uzunluğu 5 karakterd Aperiam sed voluptatum asperiores labore vero ab, animi quo quibusdam minus blanditiis
# tempora totam! Veniam autem dignissimos neque similique velit illum voluptas. en küçük ise şifreniz çok kısa 5
# karakterden daha büyük ise de şifreniz güvenlidir mesajı
# almak istiyoruz

get_password = input("Lütfen şifreninizi giriniz...: ")
password_length = len(get_password)

if password_length <= 5:
    print("Password is too short ")
else:
    print("Password is quite safety ")

# if bloklarını else olmadan tek başına sadece koşul True iken çalışacak şekilde de ayaralayabiliriz illa ki else koymak
# zorunda değiliz
anyword = input("Herhangi bir kelime girin:")
if len(anyword) == 5:
    print("Doğru sayıda karakter girdiniz...")

