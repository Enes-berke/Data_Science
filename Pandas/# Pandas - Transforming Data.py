# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 01:39:51 2023

@author: hp
"""

# Pandas - Transforming Data

import pandas as pd


dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)
dataFrame1["yeni feature"] = [-1 , -2 , -3 , -4 , -5 , -6]


dataFrame1["list_comp"] = [ each*2 for each in dataFrame1.AGE] # yaşlari kullanarak yeni bir columns oluşturmak istiyoruz
print("Yeni columns ==>\n" , dataFrame1)

# Yeni columns ==>
#      NAME  AGE  MAAS  yeni feature  list_comp
# 0    ali   15   100            -1         30
# 1   veli   16   150            -2         32
# 2  kenan   17   240            -3         34
# 3  hilal   33   350            -4         66
# 4   ayse   45   110            -5         90
# 5  evren   66   220            -6        132


# apply()

def fonk(AGE):
    return AGE*2
    
dataFrame1["apply_metodu"] = dataFrame1.AGE.apply(fonk)

#     NAME  AGE  MAAS  yeni feature  list_comp  apply_metodu
# 0    ali   15   100            -1         30            30
# 1   veli   16   150            -2         32            32
# 2  kenan   17   240            -3         34            34
# 3  hilal   33   350            -4         66            66
# 4   ayse   45   110            -5         90            90
# 5  evren   66   220            -6        132           132
