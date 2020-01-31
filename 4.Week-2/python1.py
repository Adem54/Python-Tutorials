def en_buyuk(liste):
    maksimum = liste[0]
    for eleman in liste:

        if maksimum < eleman:
            maksimum = eleman
    return maksimum


print(en_buyuk([12, 34, 55, 77, 33]))
print(en_buyuk([0, 9, 3, 100]))
