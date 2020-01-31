"""
2 tane liste'yi parameter olarak alan, bu listeleri birlestirerek tek bir liste olusturan ve olusan
bu listeyi geri donen merge(liste1, liste2) fonksiyonunu yaziniz.
merge fonksiyonun geri donecegi listede bir eleman birden fazla yer almamali, yani bir eleman
hem liste1 hem de liste2'de yer aliyorsa, bu eleman olusturulacak listeye sadece 1 kez eklenmeli.
Ayrıca listelerin kendi içinde de aynı eleman birden fazla ise ordakilerde benzersiz olacak şekilde birleştirirlmeli
liste1= [2, 5 ,6 ,7 , 10]
liste2= [5, 6, 9, 8]

print(merge(liste1, liste2))
[2, 5, 6, 7, 10, 9, 8]
Peki aynı liste içerisinde tekrar eden değerler  olursa ne olacak...
"""


# Önce liste1 i benzersiz hale getirip sonra diğer liste ile karşılaştıralım
# Bir listeyi benzersiz liste haline getiren fonksiyonu yazdık burda
def unique_list(liste1):
    unique_liste1 = []
    for eleman in liste1:
        if eleman not in unique_liste1:
            unique_liste1.append(eleman)
    return unique_liste1


liste11 = [2, 5, 2, 6, 7, 5, 10]
liste22 = [5, 6, 9, 8]

print(unique_list(liste11))


def merge(liste1, liste2):
    unique_liste1 = unique_list(liste1)
    unique_liste2 = unique_list(liste2)
    merge_list = unique_liste1 + unique_liste2
    merge_list = unique_list(merge_list)
    merge_list.sort()
    return merge_list


liste11 = [2, 5, 2, 6, 7, 9, 5, 10]
liste22 = [2, 5, 6, 9, 8, 10, 11, 14]
print(merge(liste11, liste22))

liste3 = [1, 3, 5]
liste4 = [7, 9, 11]
liste5 = liste3 + liste4
print(liste5)
