# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 03:02:27 2023

@author: hp
"""

# Pandas - Indexing and Slicing Data Frames



import pandas as pd

dictionary = {"İsim" : ("Enes" , "Alper" , "Eren" , "Furkan" , "Muhammed" , "Emirhan" , "Ali"),
              "Yas" :(19 , 20 , 21 , 19 , 19 , 22 , 18),
               "Maas" : (1750 , 1700 , 1000 , 1250 , 1400 , 750 , 1500) }

dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1["Yas"])

# 0    19
# 1    20
# 2    21
# 3    19
# 4    19
# 5    22
# 6    18
# Name: Yas, dtype: int64

print(dataFrame1.Yas)

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6,-7]
# ValueError: Length of values (6) does not match length of index (7)
# eklediginiz yeni feature ile dataframe satır sayıları eşit olmak zorundadir

print(dataFrame1.yeni_feature)

print(dataFrame1.loc[:, "Yas"]) # 1 den son satira kadar yaş sutunun yazdir


# 0    19
# 1    20
# 2    21
# 3    19
# 4    19
# 5    22
# 6    18
# Name: Yas, dtype: int64


print(dataFrame1.loc[:3, "Yas"]) # 1. satirdan 3. satira kadar yaslari yazdir
# pandas = > [1:5] 1 ve 5 degerleri dahildir !!


# 0    19
# 1    20
# 2    21
# 3    19
# Name: Yas, dtype: int64


print(dataFrame1.loc[:3, "İsim":"Maas"]) # yazdiginiz başliklerin sirasi önemlidir dikkat ediniz !!!


#      İsim  Yas  Maas
# 0    Enes   19  1750
# 1   Alper   20  1700
# 2    Eren   21  1000
# 3  Furkan   19  1250


print(dataFrame1.loc[:3, ["Yas","İsim"]])


#    Yas    İsim
# 0   19    Enes
# 1   20   Alper
# 2   21    Eren
# 3   19  Furkan


print(dataFrame1.loc[::-1,:]) # satirlari tersten yazdir


#     İsim  Yas  Maas  yeni_feature
# 6       Ali   18  1500            -7
# 5   Emirhan   22   750            -6
# 4  Muhammed   19  1400            -5
# 3    Furkan   19  1250            -4
# 2      Eren   21  1000            -3
# 1     Alper   20  1700            -2
# 0      Enes   19  1750            -1


print(dataFrame1.loc[::-1,::-1]) # satirlari ve sutunlari tersten yazdir


#   yeni_feature  Maas  Yas      İsim
# 6            -7  1500   18       Ali
# 5            -6   750   22   Emirhan
# 4            -5  1400   19  Muhammed
# 3            -4  1250   19    Furkan
# 2            -3  1000   21      Eren
# 1            -2  1700   20     Alper
# 0            -1  1750   19      Enes


print(dataFrame1.loc[:,:"Yas"]) # ilk satirdan son satira kadar  - ilk sutundan Yas sutununa kadar


#        İsim  Yas
# 0      Enes   19
# 1     Alper   20
# 2      Eren   21
# 3    Furkan   19
# 4  Muhammed   19
# 5   Emirhan   22
# 6       Ali   18


print(dataFrame1.loc[:,"İsim"])


# 0        Enes
# 1       Alper
# 2        Eren
# 3      Furkan
# 4    Muhammed
# 5     Emirhan
# 6         Ali


print(dataFrame1.iloc[:,2]) # butun satirlar index 2 olan sutun

# 0    1750
# 1    1700
# 2    1000
# 3    1250
# 4    1400
# 5     750
# 6    1500
# Name: Maas, dtype: int64


# loc = location
# iloc = integer location







