# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 00:52:24 2023

@author: hp
"""

# Matplotlib - Subplots


import pandas as pd


df = pd.read_csv(r"C:\Users\hp\Desktop\Matplotlib\iris.csv")


import matplotlib.pyplot as plt


df1 = df.drop(["Id"],axis=1) # Id leri data dan çıkartmış olduk.


setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

# plt.plot(setosa.Id , setosa.PetalLengthCm , color = "red" , label = "setosa")
# plt.plot(versicolor.Id , versicolor.PetalLengthCm , color = "blue" , label = "versicolor")
# plt.plot(virginica.Id , virginica.PetalLengthCm , color = "black" , label = "virginica")
# plt.xlabel("Id")
# plt.ylabel("PetalLengthCm")
# plt.legend() # label = ne çizdiriyoruz ==> legend ise grafiğe koymamızı sağlıyor
# plt.show()


df1.plot(grid = True) # arka plan kareli hale geliyor
plt.show()



df1.plot(grid = True , linestyle = ":") 
# graid = True  ==> arka plan kareli hale geliyor
# linestyle ":" ==> grafik çizgileri : şeklinde yazıldı
plt.show()



df1.plot(grid = True , alpha = 0.5)
# alpha = 0.5 ==> çizgilerin saydamlığını belirliyor 
plt.show()


# Subplots Kısmı !!!


df1.plot(grid = True , alpha = 0.9 , subplots = True)
# alpha = 0.9 ==> çizgilerin saydamlığını belirliyor 
plt.show()

# grafikte yer alan 4 parçayı, 4 farklı grafiğe bölerek gösterir.





plt.subplot(3 , 1 , 1)
plt.plot(setosa.Id , setosa.PetalLengthCm , color = "red" , label = "setosa")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()


plt.subplot(3 , 1 , 2)
plt.plot(versicolor.Id , versicolor.PetalLengthCm , color = "blue" , label = "versicolor")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()


plt.subplot(3 , 1 , 3)
plt.plot(virginica.Id , virginica.PetalLengthCm , color = "black" , label = "virginica")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
