# liste.append(7) liste listesinin sonuna eleman ekler
# meyveler.insert(2, "kivi") bu da meyveler listesinin 2. sırada elemanı olarak "kivi" yi ekler
# liste.index("elma") indisi buluruz

def oncesine_ekle(liste, referans_eleman, yeni_eleman):

    liste.insert(liste.index(referans_eleman), yeni_eleman)


def ardina_ekle(liste, referans_eleman, yeni_eleman):
    liste.insert(liste.index(referans_eleman) + 1, yeni_eleman)


meyveler = ["elma", "muz", "portakal", "mandalina"]
print("Önce " + str(meyveler))

oncesine_ekle(meyveler, "portakal", "limon")
ardina_ekle(meyveler, "elma", "kivi")

print("Sonra " + str(meyveler))
