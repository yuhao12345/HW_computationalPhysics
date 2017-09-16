# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:00:22 2017

@author: user
"""
import numpy as np
import pylab

def logistic(r,x):
    return r,r*x*(1-x)

x=0.5
r_array=np.arange(1,4,0.01)
x_array=[]
for r in r_array:
    for i in range(2000):
        (r,x)=logistic(r,x)
    x_array.append(x)
pylab.plot(x_array,r_array,"ko")
pylab.xlabel("x")
pylab.ylabel("r")
pylab.xlim(-0.1,1.1)
pylab.ylim(0.8,4.3)
pylab.show()


# edge of chaos is around 3.5
# fixed point doesn't move when we increase the iteration time
# choos point appears as scattering point in figtree
