# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 01:20:41 2023

@author: hp
"""

# Pandas - Drop and Concatenating

import pandas as pd


dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)
dataFrame1["yeni feature"] = [-1 , -2 , -3 , -4 , -5 , -6]


dataFrame1.drop(["yeni feature"], axis=1 ,inplace=True) # inplace = True demezsek drop eder fakat print(dataFrame1) dedigimiz zaman 
                                                        # yeni feature tekrardan dataFrame de gözükür
                                                        # inplace=True ile bu işlem kalıcı hale gelmiş oluyor

# axis = 1 ==> sutun drop et
# axis = 0 ==> soldan sağa satır drop et

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

# data1
# Out[20]: 
#     NAME  AGE  MAAS  yeni feature
# 0    ali   15   100            -1
# 1   veli   16   150            -2
# 2  kenan   17   240            -3
# 3  hilal   33   350            -4
# 4   ayse   45   110            -5

# data2
# Out[21]: 
#     NAME  AGE  MAAS  yeni feature
# 1   veli   16   150            -2
# 2  kenan   17   240            -3
# 3  hilal   33   350            -4
# 4   ayse   45   110            -5
# 5  evren   66   220            -6

# vertical = yukaridan aşagiya birleştirme (axis = 0 yazilir)

data_concat = pd.concat( [data1 , data2] , axis=0)
print("Birleştirme ==>\n " , data_concat)

# Birleştirme ==>
#       NAME  AGE  MAAS  yeni feature
# 0    ali   15   100            -1
# 1   veli   16   150            -2
# 2  kenan   17   240            -3
# 3  hilal   33   350            -4
# 4   ayse   45   110            -5
# 1   veli   16   150            -2
# 2  kenan   17   240            -3
# 3  hilal   33   350            -4
# 4   ayse   45   110            -5
# 5  evren   66   220            -6

# horizontal = axis = 1 yazilir

age = dataFrame1.AGE
maas = dataFrame1.MAAS

data_h_concat = pd.concat([ age , maas] , axis=1)
print("Birleştirme - 2 ==>\n " , data_h_concat)

# Birleştirme - 2 ==>
#      AGE  MAAS
# 0   15   100
# 1   16   150
# 2   17   240
# 3   33   350
# 4   45   110
# 5   66   220



















