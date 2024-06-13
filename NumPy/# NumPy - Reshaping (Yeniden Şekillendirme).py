# Yeniden Şekillendirme (Reshaping)

import numpy as np
from numpy import *


array_1 = np.random.randint(1, 15, size = 12) # 1 - 15 arasinda 12 elemandan oluşan bir array oluştur. 

array_2 = array_1.reshape(4, 3) # oluşturdugun bu arrayi ( reshape komutu ile ) 4 e 3 lük bir matrise dönüştür

# Çevirecegimizin matrisin eleman sayilari birbirleri ile uyumlu olmali. 12 elemandan oluşan bir arrayi 12 elemanli bir matrise çevirmek zorundayiz.

print("Array 1 ==> " , array_1)

print("Array 2 ==> " , array_2)
