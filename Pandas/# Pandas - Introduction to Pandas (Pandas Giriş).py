# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 01:34:30 2023

@author: hp
"""

# Pandas - Introduction to Pandas (Pandas Giriş)

# pip show numpy
# pip show pandas - bu komutlar ile kütüphane bilgisayara kurulu mu ögrenilebilir.

import pandas as pd

dictionary = {"İsim" : ("Enes" , "Alper" , "Eren" , "Furkan" , "Muhammed" , "Emirhan" , "Ali"),
              "Yas" :(19 , 20 , 21 , 19 , 19 , 22 , 18),
               "Maas" : (1750 , 1700 , 1000 , 1250 , 1400 , 750 , 1500) }

DataFrame1 = pd.DataFrame(dictionary)

head = DataFrame1.head()
tail = DataFrame1.tail()


print("DataFrame ==>\n " , DataFrame1)

print("Bastan 5 satir ==>\n " , DataFrame1.head)

print("Sondan 5 satir ==>\n " , DataFrame1.tail)

print("Bastan 6 satir ==>\n " , DataFrame1.head(6))



