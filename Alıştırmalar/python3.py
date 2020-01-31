# SORU-3


# Asagidaki desenleri while dongusu kullanarak olusturacak python programlarini yaziniz. Her programda yalnizca
# 1 tane while dongusu kullanabilirsiniz.

# 1. Desen
# -------------------
# *
# **
# ***
# ****
# *****
# ------------------

# 2. Desen
# ------------------
#    *
#   ***
#  *****
# *******
# *********
# ------------------

# 3. Desen
# ------------------
#    *
#   ***
#  *****
# *******
# *********
# *******
#  *****
#   ***
#    *
# ------------------

# 1. Desen
sayac = 1
while sayac < 6:
    print("*" * sayac)
    sayac = sayac + 1

# 2. Desen

sayi = 1
sayac = 6
while sayi < 10 and sayac > 1:
    print(sayac * " " + "*" * sayi)
    sayi = sayi + 2
    sayac = sayac - 1

"""
Birden fazla satır yorum olacaksa bu şekilde  yapabiliriz

dfasdf
"""
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&6")
# 3. Desen

sayi = 1
sayac = 6
while sayi < 10 and sayac > 1:
    print(sayac * " " + "*" * sayi)
    sayi = sayi + 2
    sayac = sayac - 1
    if sayi > 10 and sayac <= 1:
        print((sayac + 2) * " " + "*" * (sayi - 4))
        print((sayac + 3) * " " + "*" * (sayi - 6))
        print((sayac + 4) * " " + "*" * (sayi - 8))
        print((sayac + 5) * " " + "*" * (sayi - 10))

print("------------------------------------------------------------------------------------------------------")
# Bu şekilde de yapılabilir ama hangisi daha mantıklı veya daha kısa bir yöntem illaki vardır
sayi = 1
sayac = 6
while sayi < 10 and sayac > 1:
    print(sayac * " " + "*" * sayi)
    sayi = sayi + 2
    sayac = sayac - 1
    if sayi > 10 and sayac <= 1:
        sayi = 7
        sayac = 3
        print(sayac * " " + "*" * sayi)
        sayi = sayi - 2
        sayac = sayac + 1
        print(sayac * " " + "*" * sayi)
        sayi = sayi - 2
        sayac = sayac + 1
        print(sayac * " " + "*" * sayi)
        sayi = sayi - 2
        sayac = sayac + 1
        print(sayac * " " + "*" * sayi)
        sayi = 11
        sayac = 1

        """
        print((sayac + 3) * " " + "*" * (sayi - 6))
        print((sayac + 4) * " " + "*" * (sayi - 8))
        print((sayac + 5) * " " + "*" * (sayi - 10))
"""
