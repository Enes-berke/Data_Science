# Stacking Arrays (Array birleşimleri)

import numpy as np
from numpy import *

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# veritical ==> dikey birleştirme 
#array([[1, 2],
#       [3, 4]])
#array([[-1, -2],
#       [-3, -4]])
array3 = np.vstack((array1,array2))
print(array3)

# horizontal ==> yatay birleştirme
#array([[1, 2],[-1, -2],
#       [3, 4]],[-3, -4]]

array4 = np.hstack((array1,array2))
print(array4)
