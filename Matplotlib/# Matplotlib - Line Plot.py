# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 03:12:29 2023

@author: hp
"""

# Matplotlib - Line Plot


import pandas as pd


df = pd.read_csv(r"C:\Users\hp\Desktop\Matplotlib\iris.csv")


import matplotlib.pyplot as plt


df1 = df.drop(["Id"],axis=1) # Id leri data dan çıkartmış olduk.

# df1.plot()
# plt.show()

# setosa = setosa.drop(["Id"],axis=1)
# setosa.plot()
# plt.show()
# versicolor = versicolor.drop(["Id"],axis=1)
# versicolor.plot()
# plt.show()
# virginica = virginica.drop(["Id"],axis=1)
# virginica.plot()
# plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id , setosa.PetalLengthCm , color = "red" , label = "setosa")
plt.plot(versicolor.Id , versicolor.PetalLengthCm , color = "blue" , label = "versicolor")
plt.plot(virginica.Id , virginica.PetalLengthCm , color = "black" , label = "virginica")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend() # label = ne çizdiriyoruz ==> legend ise grafiğe koymamızı sağlıyor
plt.show()



df1.plot(grid = True) # arka plan kareli hale geliyor
plt.show()



df1.plot(grid = True , linestyle = ":") 
# graid = True  ==> arka plan kareli hale geliyor
# linestyle ":" ==> grafik çizgileri : şeklinde yazıldı
plt.show()



df1.plot(grid = True , alpha = 0.5)
# alpha = 0.5 ==> çizgilerin saydamlığını belirliyor 
plt.show()
















