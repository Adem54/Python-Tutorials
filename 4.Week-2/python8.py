# Bir alışveriş listesi oluşturan bir program yazmak istiyoruz. Bunun için önce her bir ürün için kullanıcıdan
# miktar soracak ve sonra da bu miktarları daha önce yazdığımız siparisleri_yazdir fonksiyonunu kullanarak yazdırmak
# istiyoruz. Bunun için
# Kullanıcıya, şu listedeki ürünlerden her birisi için kaç tane istediğini soran ve sonucu liste olarak dönen
#  siparisleri_al fonksiyonunu yazın: Cay, Kahve, Kek, Sufle, Sutlac

def siparisleri_al():
    menu_list = ["Cay", "Kahve", "Kek", "Sufle", "Sutlac"]
    siparis_list = []
    for urun in menu_list:
        siparis_list.append([urun, int(input("Kaç tane " + urun + " ihtiyacın var?"))])
    return siparis_list


def siparisleri_yazdir(siparisler):
    indis = 0

    while indis < len(siparisler):
        print(siparisler[indis][0] + ": " + str(siparisler[indis][1]))
        indis += 1

    return siparisler


siparisler = siparisleri_al()
siparisleri_yazdir(siparisler)
