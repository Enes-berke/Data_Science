# Fancy Index

import numpy as np
from numpy import *

v = np.arange(0, 40, 5) # 0 dan 40 a kadar 5 in katlarini yazdır (40 haric) 0-5-10-15-20-25-30-35 

print(v)
print(v[1])
print(v[4]) # bu şekilde sira ile girmek üşendirici oldugu için aşagidaki yolu kullaniriz ==>

index = [1, 2, 3] 

print(v[index]) # v[index] demek => v[1] - v[2] - v[3] ifadelerinin daha kolay ifade edilmiş şeklidir.

# 1 - 2 - 3 indexteki sayılar bu şekilde daha sağlikli bir şekilde ifade edilmiş olur. 
