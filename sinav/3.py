"""
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları alt alta ekrana bastırın.
"""
sayac = 1
while sayac < 100:
    if sayac % 3 == 0:
        print(sayac)
    sayac += 1
