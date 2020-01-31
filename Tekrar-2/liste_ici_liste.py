ogrenciler = [["baris", [3.5, 4, 2]], ["ayse", [3, 4, 4]], ["onur", [0, 2.85, 3]]]

"""
onur'un son notunu ekrana yazdır
onur'un notlarını onurun_notlari değişkenine sakla
onurun_notlari değişkenini kullanarak onur'un son notunu ekrana yazdır
"""

onur = ogrenciler[2]
onurun_notlari = onur[1]
onurun_son_notu = onurun_notlari[2]

print("Onur: "+str(onur))
print("onurun_notlari: "+ str(onurun_notlari))
print("onurun_son_notu: "+str(onurun_son_notu))