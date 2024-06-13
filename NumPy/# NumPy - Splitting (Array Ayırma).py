# NumPy - Splitting (Array Ayırma)

import numpy as np
from numpy import * 

x = np.array([1,2,3,4,5,99,88,77,6,7,8,9])

print ( np.split ( x , [ 5 , 8 ] ) )

# x i split et. önce 5 e kadar ayir . Sonra 5 ten 8 e kadar bir kez daha ayir.
# [array([1, 2, 3, 4, 5]), array([99, 88, 77]), array([6, 7, 8, 9])]

a , b , c =  np.split ( x , [ 5 , 8 ] ) 

print("\n a ==> " , a)
print("\n b ==> " , b)
print("\n c ==> " , c)

