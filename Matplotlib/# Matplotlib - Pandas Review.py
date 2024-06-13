# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 01:47:29 2023

@author: hp
"""
# Matplotlib - Pandas Review

# matplotlib kutuphanesi
# gorsellestime kotuphanesi
# line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Desktop\Matplotlib\iris.csv")

print("Columns ==> " ,df.columns)
# species ==> tür
# SepalLengthCm
# SepalWidthCm 
# PetalLengthCm
# PetalWidthCm
# Species


# Çok fazla columns olursa columnsların sayisini nasil buluruz ??
print(df.Species.unique())


print(df.Species.unique())
# ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']

print(df.info())

print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 150 entries, 0 to 149
# Data columns (total 6 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   Id             150 non-null    int64  
#  1   SepalLengthCm  150 non-null    float64
#  2   SepalWidthCm   150 non-null    float64
#  3   PetalLengthCm  150 non-null    float64
#  4   PetalWidthCm   150 non-null    float64
#  5   Species        150 non-null    object 
# dtypes: float64(4), int64(1), object(1)
# memory usage: 7.2+ KB
# None


print(df.describe()) # 3 türünde bulunduğu datayı karşılaştırdık

# print(df.describe())
#                Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
# count  150.000000     150.000000    150.000000     150.000000    150.000000
# mean    75.500000       5.843333      3.054000       3.758667      1.198667
# std     43.445368       0.828066      0.433594       1.764420      0.763161
# min      1.000000       4.300000      2.000000       1.000000      0.100000
# 25%     38.250000       5.100000      2.800000       1.600000      0.300000
# 50%     75.500000       5.800000      3.000000       4.350000      1.300000
# 75%    112.750000       6.400000      3.300000       5.100000      1.800000
# max    150.000000       7.900000      4.400000       6.900000      2.500000


setosa = df[df.Species == "Iris-setosa"]
print("setosa ==>\n" , setosa ) 

versicolor = df[df.Species == "Iris-versicolor"]
print("versicolor ==>\n" , versicolor ) 

virginica = df[df.Species == "Iris-virginica"]
print("virginica ==>\n" , virginica ) 



print(setosa.describe()) 
print(versicolor.describe())
print(virginica.describe())
# türleri, kendi türleri ile karşılaştırdık (setosalar, setosalar iler karşılaştırılması yapılmış oldu)




