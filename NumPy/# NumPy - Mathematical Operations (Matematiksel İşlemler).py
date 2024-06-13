# Matematiksel Işlemler (Mathematical Operations)

import numpy as np
from numpy import *

a = np.array([1, 2, 3, 4, 5])

print("dizideki elemanlarin toplami ==> " , np.sum(a)) # dizideki elemanlarin toplami ==> 1+2+3+4+5 => 15
print("min deger ==> " , np.min(a)) # min deger ==> 1
print("max deger ==> " , np.max(a)) # max deger ==> 5
print("standart sapma ==> " , np.std(a)) # standart sapma
print("varyans ==> " , np.var(a)) # varyans
print("min degerin indeksi ==> " , np.argmin(a)) # min degerin indeksi ==>  min deger (1) => 1 in indeksi => 0
print("max degern indeksi ==> " , np.argmax(a)) # max degern indeksi 
print("median ==> " , np.median(a)) # median

print("Bütün elemanlarin karesi ==> " , a**2 ) 

print("Bütün elemanlari 5 ile topla ==> " , np.add(a , 5)) 
print("Bütün elemanlarin 2 den farkini al ==> " , np.subtract(a, 2)) 



