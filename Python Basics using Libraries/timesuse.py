# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:37:56 2019

@author: DEVANSH JAIN
"""

import time
print('Sleep')
time.sleep(3)
print('Woke Up')
"""
Numpy-Data Computation,Numerical Analysis,MAthematical computing

matplotlib-Data Visualization,Data Graphical Representation

Pandas-Data Exploring,Handling and fetching

scikit-learn-Data prediction,regression,machine learning algorithm

"""
import numpy
data=numpy.random.randint(5,10,(10,5))
c=['temperature','humidity','gas','pressure','light']
import pandas
dates=pandas.date_range('20170927',periods=10)
df=pandas.DataFrame(data,index=dates,columns=c)


