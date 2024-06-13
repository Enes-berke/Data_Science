# NumPy Basics Operations 

import numpy as np
from numpy import * 

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a)) # a nin sinusunu al

print(a < 2) # True False False

aa = np.array([[1,2,3],
               [4,5,6]])

bb = np.array([[1,2,3],
               [4,5,6]])

print("a x b ==> " , a*b)

# print(aa.dot(bb)) # Matrix çarpimlarda aa satır sayısı bb sutun sayısına eşit olmalı bu sebeple bu işlemde hata alırız

print("==> \n" , aa.dot(bb.T)) # bb.T ==> b matrixinin transpozesini alma demektir.



aaa = np.random.random((5,5)) # 5 e 5 lik 0 ile 1 arasinda sayi üretmek.
print("Random 5 e 5 ==> " , aaa)

aaa.sum() # Arayin içindeki tüm degerlerin toplami ==>
aaa.max() # Arayin içindeki max degeri ==>
aaa.min() # Arayin içindeki min deger ==>

aaa.sum(axis=0) # Sutunlara göre toplama. Sadece sutun olarak toplama islemi yapilir.
aaa.sum(axis=1) # Satirlar kendi aralarinda toplanir

print("Arayin içindeki tüm degerlerin toplami ==>" , aaa.sum() )
print("Arayin içindeki max degeri ==>" , aaa.max())
print("Arayin içindeki min deger ==>" , aaa.min())
print("Sutunlara göre toplama ==>" , aaa.sum(axis=0))
print("Satirlar kendi aralarinda toplanir ==>" , aaa.sum(axis=1) )

print("Matrixin karekoku ==>" , np.sqrt(aaa))
print("Matrixin karesi ==>" , np.square(aaa)) # a**2

print("İki matrixin toplamini ifade eder ==> " , np.add(aaa , aaa))