# NumPy Basics

"""
Traceback (most recent call last):
  File "c:Users hp Desktop # Numpy Basics.py", line 3, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy' ==> Bu hatayi aliyorsaniz eger 

1 ==> Başlat menüsünden veya terminalden bir komut istemcisini açin.

2==> Aşağidaki komutu kullanarak NumPy'i yükleyin:

pip install numpy

2.1==> Eğer Python 3 kullaniyorsaniz, bazen pip3 komutunu kullanmaniz gerekebilir:
pip3 install numpy
"""


import numpy as np # Bu tanimlama ile artik numpy paketi program içerisinde np ismiyle temsil edilecektir.

from numpy import * # Bu tanimlama ile numpy paketi içerisindeki tüm komutlar doğrudan çağrilabilir.

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(array.shape) # 15 e 1 lik bir vektör (15,)

a = array.reshape(3,5) # 3 satir ve 5 sutunden oluşan bir array haline getir.

print("shape =>", a.shape)

print("Dimension =>",a.ndim) # Kaç boyutlu olduğunu gösterir. 3 e 5 ==> 2 boyutlu

print("Data typr =>" , a.dtype.name) # Arrayin içindeki data typlerin isimleri nedir ??  => int32

print("Size => " , a.size) #Reshape den önceki boyutunu verir  ==> 15 (1 e 15 lik bir vektördü)

print("type => " ,type(a)) # => type =>  <class 'numpy.ndarray'> 

array1 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,8,7,5]]) # Reshape kullanmadan matrix oluşturma

matrix0 = np.zeros((3,4)) # 3 e 4 lük sıfırlardan oluşan matrix oluşturma

matrix0[0][0] = 5
print(matrix0)

matrix1 = np.ones((3,4)) # 3 e 4 lük birlerden oluşan matrix oluşturma
print(matrix1)

matrix_ = np.empty((5,4)) # 3 e 4 lük boşlardan oluşan matrix oluşturma
print(matrix_)

b = np.arange(0 , 90 , 12) # 0 - 90 arasındaki sayıları 12 şer olarak yazdır. Son sayılar genelde dahil olmaz 
print("==> " , b)

c = np.linspace(0 , 50 , 20) # 0 - 50 arasında araya 20 tane sayı yazdır. Son sayı dahil.
print("==> " , c)


array2 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,8,7,5]]) 

print("Bellek adresi ==> " , array2.data) # Dizinin bellek adresini verir.
print("Eleman sayisi ==> " , array2.size) # Dizinin eleman sayısını verir.

print("Tek boyutlu hali ==> " , array2.ravel()) # Matrisi tek boyutlu diziye çevirir.
#print(array2.flat)  Matrisi tek boyutlu diziye çevirir.