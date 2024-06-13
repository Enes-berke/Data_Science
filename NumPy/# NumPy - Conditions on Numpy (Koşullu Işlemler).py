# NumPy'da Koşullu İşlemler (Conditions on Numpy)

import numpy as np
from numpy import *

a = np.array([1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,100])

# Vektörümüzde 30 dan büyük degerleri yazdiralim

print("30 dan büyük degerler ==> " , a[a>30] )
print("30 dan kucuk degerler ==> " , a[a < 30] )
print("33 e esit olmayan degerler degerler ==> " , a[a != 33] )
print("22 ye esit olan deger yazdir ==> " , a[a == 22] )
print("30 e eşit ve 33 den büyük degerler ==> " , a[a >= 33] )
