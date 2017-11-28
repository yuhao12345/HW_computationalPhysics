# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:16:03 2017

@author: user
"""
from random import random
import numpy as np

n=int(input('sample number N= '))

def ran():
    return random()**2

def f(x):
    return 1/(np.exp(x)+1)

sum=0
for i in range(n):
    sum+=f(ran())

print('I=',sum/n*2)