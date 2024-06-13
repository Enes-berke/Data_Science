# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:44:40 2023

@author: hp
"""

# Pandas - List Comprehension

import pandas as pd


dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)
dataFrame1["yeni feature"] = [-1 , -2 , -3 , -4 , -5 , -6]

ortalama_maas = dataFrame1.MAAS.mean()

# ortalama_maas_np = np.mean(dataFrame1.MAAS)


dataFrame1["Maas_seviyeleri"] = [ "yüksektir" if each > ortalama_maas  else "düşüktür" for each in dataFrame1.MAAS]

# MAAS SEVİYELERİ NASIL ==>
# 0     düşüktür
# 1     düşüktür
# 2    yüksektir
# 3    yüksektir
# 4     düşüktür
# 5    yüksektir
# # Name: Maas_seviyeleri, dtype: object


#for each in dataFrame1.MAAS:
#    if(ortalama_maas > each):
#        print("dusuk")
#    else:
#        print("yukse")
        

dataFrame1.columns # sutun başlıklarının isimlerini verir


dataFrame1.columns = [ each.lower() for each in dataFrame1.columns] 
#Out[8]: Index(['name', 'age', 'maas', 'maas_seviyeleri'], dtype='object')

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]

# dataFrame1. columns ile sutun başliklarina bakıyoruz ==> Maas Age vs

# if => eğer {(each.split) arada boşluk bulunanlari ayri kelime olarak ele alir.}
#            ele alinan başlikta bir den fazla kelime var ise demek ki kelimeler arasi boşluk vardır
#            each.split()[0] ==> kelimenin 0. indeksini yani ikiye bölünen kelimenin ilk kısmını al (yeni feature ==> yeni ksımı alınır)
#            +"_" ==> ilk alinan kelime artı _ işareti
#            +each.split()[1]  => kelimenin 1. indeksi alınır (yeni feature ==> feature kısmı alinmiş olur)
    

print("Yeni columns ==>" , dataFrame1.columns)

# Yeni columns ==> Index(['name', 'age', 'maas', 'maas_seviyeleri', 'yeni_feature'], dtype='object')


