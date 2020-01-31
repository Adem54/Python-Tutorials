# Yani,
# alt_str("merhaba", 0, 1) yazdığımızda "m" dönmeli.
# alt_str("merhaba", 2, 4) yazdığımızda "rh" dönmeli.

def alt_str(str, bas_indis, bit_indis):
    new_str = ""

    while bas_indis < bit_indis:
        new_str += str[bas_indis]
        bas_indis += 1
    return new_str


mesaj = "Merhaba, programci!"
print(alt_str(mesaj, 0, 7))  # Merhaba yazmalı
print(alt_str(mesaj, 4, 7))  # aba yazmalı
print(alt_str(mesaj, 9, 18))  # programci yazmalı
