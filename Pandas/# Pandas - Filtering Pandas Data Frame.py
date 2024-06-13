# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:34:57 2023

@author: hp
"""

# Pandas - Filtering Pandas Data Frame

import pandas as pd


dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)


filtre1 = dataFrame1.MAAS > 200
print("filtre1 ==>\n" , filtre1)


# filtre1 ==> 
# 0    False
# 1    False
# 2     True
# 3     True
# 4    False
# 5     True
# Name: MAAS, dtype: bool


filtrelenmis_data = dataFrame1[filtre1]
print("filtrelenmis_data ==>\n" , filtrelenmis_data)


# filtrelenmis_data ==>
#      NAME  AGE  MAAS
# 2  kenan   17   240
# 3  hilal   33   350
# 5  evren   66   220


filtre2 = dataFrame1.AGE <20

dataFrame1[filtre1 & filtre2] # iki filtreyi birleştirme

#  NAME  AGE  MAAS
# 2  kenan   17   240

print(dataFrame1[dataFrame1.AGE > 60])

#     NAME  AGE  MAAS
# 5  evren   66   220

