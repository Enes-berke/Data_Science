# Index Seçimi (Index Selection)

import numpy as np
from numpy import *

a = np.random.randint(7 , 23, 10) # 7 - 23 arasinda 10 elemanli bir array

print("a ==> " , a)

print("a[0] ==>" , a[0])
print("a[0:5] ==>" , a[0:5]) # 0. indexten 5. index e kadar. Ama 5. index dahil değil ==> 0 - 1 - 2 - 3 - 4 
a[0] = 999 # 0 index 999 eşitlenmiş oldu

print("a ==> " , a)


m = np.random.randint(12 , 55 , (3 , 5)) # 12 - 55 arasinda 3 satir ve 5 sutunden oluşan 15 elemanli br array (matrix) oluştur.

print("\n\n m[] ==>" , m)

print("\nm[0, 0] ==>" , m[0, 0]) # satir = 0 / sutun = 0

print("\nm[1, 1]" , m[1, 1]) # satir = 1 / sutun = 1

print("\nm[2, 3] ==>" ,m[2, 3]) # satir = 2 / sutun = 3

m[2, 3] = 999

print("\nm[2, 3] ==>" ,m[2, 3]) # Değişmiş oldu .


print("\nm[:, 0] ==>" ,m[:, 0]) # satir = 0 dan son satira kadar  / sutun = 0 [{==> 0. satir 0. sutun / 1. satir 0. sutun / 2. satir 0. sutun .....}]

print("\nm[1, :] ==> " , m[1, :]) # satir = 1 / sutun = 0 dan son sutuna kadar  [{==> 1. satir 0. sutun / 1. satir 1. sutun / 1. satir 2. sutun .....}]

print("\nm[0:2, 0:3] ==> " , m[0:2, 0:3]) # satir = 0 - 1 / sutun = 0 - 1 - 2

# satir = 0 sutun = 0
# satir = 0 sutun = 1
# satir = 0 sutun = 2
# satir = 1 sutun = 0
# satir = 1 sutun = 1
# satir = 1 sutun = 2


