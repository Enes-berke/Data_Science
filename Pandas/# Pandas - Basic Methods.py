# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:26:24 2023

@author: hp
"""
# Pandas Basic Methods

import pandas as pd

dictionary = {"İsim" : ("Enes" , "Alper" , "Eren" , "Furkan" , "Muhammed" , "Emirhan" , "Ali"),
              "Yas" :(19 , 20 , 21 , 19 , 19 , 22 , 18),
               "Maas" : (1750 , 1700 , 1000 , 1250 , 1400 , 750 , 1500) }

DataFrame1 = pd.DataFrame(dictionary)

head = DataFrame1.head()
tail = DataFrame1.tail()


print("DataFrame ==>\n " , DataFrame1)

print("Bastan 5 satir ==>\n " , DataFrame1.head)

print("Sondan 5 satir ==>\n " , DataFrame1.tail)

print("Bastan 6 satir ==>\n " , DataFrame1.head(6))



print(DataFrame1.columns) # sutunlarin isimlerini verir

print(DataFrame1.info()) # 

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7 entries, 0 to 6
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   İsim    7 non-null      object
#  1   Yas     7 non-null      int64 
#  2   Maas    7 non-null      int64 
# dtypes: int64(2), object(1)
# memory usage: 296.0+ bytes
# None


print(DataFrame1.dtypes)

# İsim    object
# Yas      int64
# Maas     int64
# dtype: object

print(DataFrame1.describe())  # numeric feature = columns (age,maas)

#              Yas         Maas
# count   7.000000     7.000000
# mean   19.714286  1335.714286
# std     1.380131   364.822201
# min    18.000000   750.000000
# 25%    19.000000  1125.000000
# 50%    19.000000  1400.000000
# 75%    20.500000  1600.000000
# max    22.000000  1750.000000

