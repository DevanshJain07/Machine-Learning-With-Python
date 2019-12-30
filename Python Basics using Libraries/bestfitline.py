# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:37:09 2019

@author: DEVANSH JAIN
"""

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs=np.array([1,2,3,4,5,6], dtype=np.float64)
ys=np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m=( ((mean(xs) * mean(ys)) - mean(xs*ys))/
       ((mean(xs)*mean(xs))-mean(xs*xs)) )
       
    b=mean(ys) - m*mean(xs)
    return m , b

m,b=best_fit_slope_and_intercept(xs,ys)

regression_line=[(m*x)+b for x in xs]

plt.scatter(xs,ys)
plt.plot(xs, regression_line)
plt.show()
