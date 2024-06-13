# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 00:34:15 2023

@author: hp
"""

# Matplotlib - Histogram

import pandas as pd


df = pd.read_csv(r"C:\Users\hp\Desktop\Matplotlib\iris.csv")


import matplotlib.pyplot as plt


df1 = df.drop(["Id"],axis=1) # Id leri data dan çıkartmış olduk.



setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]



plt.hist(setosa.PetalLengthCm , color = "red" , label = "setosa" , bins = 25) # degerlerin yogunlukları hakkında bilgi verir
plt.legend()
plt.xlabel("PetalLengthCm-Deger")
plt.ylabel("Yoğunluk")
plt.show()

# bins = degerleri hıstogram grafiginin kalinligini ayarlamada yardimci olur


