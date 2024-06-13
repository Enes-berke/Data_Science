# İndexing and Slicing

import numpy as np
from numpy import *

array = np.array([1,2,3,4,5,6,7])   #  vector dimension = 1

print(array[2]) # => 3 

print(array[0:4]) # => 1 - 2 - 3 - 4 (0. indexten 4. indexe kadar yazdırır)

reverse_array = array[::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,1]) # ==> 7

print(array1[:,1]) # ==> 2 - 7


print(array1[1,1:4]) # ==> 7 - 8 - 9


print(array1[-1,:]) # ==> 6 - 7 - 8 - 9 - 10
print(array1[:,-1]) # ==> 5 - 10