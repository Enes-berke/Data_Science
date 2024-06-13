# Shape Manipulation

import numpy as np
from numpy import *

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(array.ravel()) # Matrixi tek boyutlu - vektör hal,ne getirme

print(array.reshape(3,3)) # etki ettigi arrayı degiştirmez. Başka bir degişkene eşitlersen array başka degişken üzerinde değişmiş olur. 

array2 = array.T
print(array2) # Matrixin transpozunu alma

# array2.resize((2,3)) ==> etki ettigi arrayi değiştirir