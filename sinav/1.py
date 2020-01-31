"""
Kullanıcıdan iki tane sayı isteyin ve alınan değerleri değişkenlere saklayın
Bu değişkenlerin değerlerini birbirleriyle değiştirin
Kullanıcının girdiği iki sayıyı ekrana yazdırın
Kullanıcı sırasıyla 1 ve 10 girdiğinde, ekrana önce 10 sonra 1 yazmalı
"""

a = int(input("a:"))  # 1
b = int(input("b:"))  # 10
x = a
a = b
b = x

print(a)
print(b)
