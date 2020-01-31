"""
"Programlama" kelimesinin harflerini for döngüsü kullanarak sırayla alt alta yazdır.
Program döngüden ilk "m" harfini yazdırmadan çıksın.
Program çalıştığında ekranda "p", "r", "o", "g", "r", "a" harfleri alt alta yazılmış olacak

"""
my_string = "Programlama"
for char in my_string:
    if char == "m":
        break
    else:
        print(char)

"""
"Programlama" kelimesinin "a" harfi hariç diğer harflerini for döngüsü kullanarak sırayla yazdırın.
"""
print("---------------------------------------------------------------------------")

my_string = "Programlama"
for char in my_string:
    if char == "a":
        continue
    else:
        print(char)
