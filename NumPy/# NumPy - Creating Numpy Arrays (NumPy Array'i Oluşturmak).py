# NumPy - NumPy Array'i Oluşturmak (Creating Numpy Arrays)

import numpy as np
from numpy import *

array1 = np.array([1, 2, 3, 4, 5])

print(type(np.array([1, 2, 3, 4, 5])))


print(np.zeros(10, dtype=int)) # o lardan bir array oluşturmak

print(np.random.randint(0, 10, size=10)) # 0 - 10 arasında 10 tane elemanlı random bir array oluşturma

print(np.random.normal(10, 4, (3, 4))) # Ortalaması 10 - Standart sapması 4 olan 3'e 4'lük bir array oluşturma