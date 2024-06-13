# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 00:43:29 2023

@author: hp
"""


# Matplotlib - Bar Plot

import numpy as np

import matplotlib.pyplot as plt


x = np.array(([1,2,3,4,5,6,7,8,9,10]))

y = 3 * x + 7

plt.bar( x , y , color = "green")
plt.title("y = 3 * x + 7 islemi")
plt.xlabel("X degerleri")
plt.ylabel("y degerleri")
plt.show()

# ülkelerin yıllık gelirleri gibi grafikler bu uygulama için uygundur