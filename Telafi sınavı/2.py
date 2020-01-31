"""
not_listesi = [['Ayşe', 95], ['Ali', 85]]

Sınav notları yukarıdaki formatta tutulan bir sınıf için, sınav notları ve sınıfın genel
ortalaması parametrelerini alip, geriye sınıf ortalamasının altındaki oğrencilerin isimlerini bir liste şeklinde dönen
  ortalamanin_altindakiler(notlar_listesi, sinif_ortalamasi) fonksiyonunu yazınız.

Örnek:
Input: ortalamanin_altindakiler([['Hamdi', 89], ['Ayşe', 95], ['Ali', 85]], 90)
Output: ['Hamdi', 'Ali']
"""


def ortalamanin_altindakiler(notlar_listesi, sinif_ortalamasi):
    liste2 = []

    for student in notlar_listesi:
        liste1 = []
        student_note = student[1]
        student_name = student[0]
        if student_note < sinif_ortalamasi:
            liste1.append(student_name)
            liste1.append(student_note)
            liste2.append(liste1)

    return liste2


print(ortalamanin_altindakiler([['Ayşe', 95], ['Ali', 85]], 90))
print(ortalamanin_altindakiler([['Ayşe', 95], ['Ali', 85], ['Mehmet', 75], ['Harry', 65], ["Kazım", 20]], 80))
