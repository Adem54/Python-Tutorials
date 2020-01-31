"""
Kullanıcının girdiği bir string içindeki harflerden sadece tek sayıda tekrar eden harfleri bulan bir program yazınız.

Örnek:

Girdi: aabc

Çıktı: ['b','c']

Girdi: abaabc

Çıktı: ['a','c']
"""
kelime = input("bir kelime gir")
liste = []
tekrar_eleman = []
for eleman in kelime:
    if eleman not in liste:
        liste.append(eleman)
    else:
        tekrar_eleman.append(eleman)
for eleman1 in liste:
    if eleman1 in tekrar_eleman:
        liste.remove(eleman1)

print(liste)
