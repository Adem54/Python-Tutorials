"""
not_listesi = [["Ayşe", 95], ["Ali", 85]]
Sınav notları yukarıdaki formatta tutulan bir sınıf için, tüm sınıfın genel ortalamasını geri
dönen ortalama_hesapla(notlar_listesi) fonksiyonunu yazınız.
Örnek:
Input: ortalama_hesapla([["Ayşe", 95], ["Ali", 85]])
Output: 90
"""

"""


"""


def ortalama_hesapla(notlar_listesi):
    ortalama = 0
    toplam = 0
    for sayi in range(len(notlar_listesi)):
        eleman = notlar_listesi[sayi]
        student_note = eleman[1]
        toplam = toplam + student_note
        eleman_sayisi = sayi + 1
        ortalama = round((toplam / eleman_sayisi), 2)
    return ortalama


print(ortalama_hesapla([['Ayşe', 95], ['Ali', 85]]))
print(ortalama_hesapla([['Ayşe', 95], ['Ali', 85], ['Mehmet', 75]]))
