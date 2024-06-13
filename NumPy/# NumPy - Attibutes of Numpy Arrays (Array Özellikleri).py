# NumPy - NumPy Array Özellikleri (Attibutes of Numpy Arrays)

import numpy as np
from numpy import *

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

array_1 = np.arange( 2 , 26 , 3) # 2 den başlar ve 3 er artarak 26 değerine kadar bir array oluşturu. 2 - 5 - ..... - 20 - 23

print("Array ==> " , array_1) # Array ==> [ 2  5  8 11 14 17 20 23]

print("Dizinin tipini verir ==>" , array_1.dtype )  #  int32

print("Dizinin boyutunu verir ==>" , array_1.ndim ) # 1

print("Dizinin eleman sayisini verir ==>" , array_1.size ) #  8

print("Dizinin bellek adresini verir. ==>" , array_1.data ) 

print("Dizinin boyut bilgisini verir ==>" , array_1.shape ) # (8,)


array_2 = np.array([[1,2,3],
                   [4,5,6]])

print("Dizinin boyutunu verir ==>" , array_2.ndim ) # 2

