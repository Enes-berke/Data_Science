# Convert and Copy

import numpy as np
from numpy import *

liste = [1,2,3,4]   # list

array = np.array(liste) #np.array ==> Array çevirme

liste2 = list(array) # Listeye çevirme

a = np.array([1,2,3])

b = a
print("before b ==>", b)

b[0] = 5 # ==> bu işlem ile a array içindeki deger de 5 e dönüştü ==> a - b ve c aynı alan ayrılıyor. Bu sebeple bir degişiklik hepsini etkiliyor. 

c = a

print(" a ==>", a)
print("late b ==>", b)
print(" c ==>", c)

d =  np.array([1,2,3])
print(" d ==>", d)

e = d.copy()
print(" e ==>", e)

f = d.copy()
print(" f ==>", f)
