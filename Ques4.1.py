# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:00:22 2017

@author: user
"""




def factorial(n):
    f=int(1.0)
    #f=1.0
    for i in range(1,n+1):
        f*=i
    return f
 
a=factorial(200)

print(a)


# using integer variables can get right answer, while floating-point return inf
# floating number has maximum allowed value 1e308