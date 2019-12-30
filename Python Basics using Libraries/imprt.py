# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:54:56 2019

@author: DEVANSimH JAIN
"""
import numpy

from numpy import *
m=numpy.matrix([[7,5,8],[1,2,3],[4,5,6]])
numpy.linalg.inv(m)

from numpy.linalg import *
inv(m)

#4x-6y=18
#3x+7y=25

a=numpy.array([[4,-6],[3,7]])
b=numpy.array([[18],[25]])


numpy.linalg.solve(a,b)

k=numpy.arange(2,12,2)

h=numpy.eye(3)