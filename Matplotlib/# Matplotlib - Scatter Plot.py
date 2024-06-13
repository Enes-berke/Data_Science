# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 00:23:59 2023

@author: hp
"""

# Matplotlib - Scatter Plot

import pandas as pd


df = pd.read_csv(r"C:\Users\hp\Desktop\Matplotlib\iris.csv")


import matplotlib.pyplot as plt


df1 = df.drop(["Id"],axis=1) # Id leri data dan çıkartmış olduk.



setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

# plt.scatter(setosa.PetalLengthCm , setosa.PetalWidthCm , color = "red" , label = "setosa")
# plt.legend() # label = ne çizdiriyoruz ==> legend ise grafiğe koymamızı sağlıyor
# plt.xlabel("PetalLengthCm")
# plt.ylabel("PetalWidthCm")  
# plt.title("scatter plot")
# plt.show()


plt.scatter(setosa.PetalLengthCm , setosa.PetalWidthCm , color = "red" , label = "setosa")
plt.scatter(versicolor.PetalLengthCm , versicolor.PetalWidthCm , color = "blue" , label = "versicolor")
plt.scatter(virginica.PetalLengthCm , virginica.PetalWidthCm , color = "black" , label = "virginica")

plt.legend() # label = ne çizdiriyoruz ==> legend ise grafiğe koymamızı sağlıyor
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")  
plt.title("scatter plot")
plt.show()





