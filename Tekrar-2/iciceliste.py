liste = [['Cay', 3], ['Kek', 5], ['Kahve', 2]]


def siparisler(list):
    for eleman in list:
        urun = eleman[0]
        adet = eleman[1]
        print(urun + ":" + str(adet))


liste = [['Cay', 3], ['Kek', 5], ['Kahve', 2]]
siparisler(liste)

"""
Kullanıcıya, şu listedeki ürünlerden her birisi için kaç tane istediğini soran ve sonucu liste olarak 
dönen siparisleri_al fonksiyonunu yazın: Cay, Kahve, Kek, Sufle, Sutlac
siparisler fonksiyonu bize bir liste içinde listeler döndürmeli
"""


def siparisler():
    siparis_list = []
    menu_list = ["Çay", "Kahve", "Kek", "Sufle", "Sutlac"]
    for eleman in menu_list:
        siparis = []
        adet = int(input("kaç adet " + eleman + " istersiniz"))
        siparis.append(eleman)
        siparis.append(adet)
        siparis_list.append(siparis)
    return siparis_list


print(siparisler())
"""
En son 77 de kaldım.....
"""
