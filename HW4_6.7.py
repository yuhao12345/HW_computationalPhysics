# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import copy,zeros,array,arange
from pylab import plot,show,xlabel,ylabel

def banded(Aa,va,up,down):

    # Copy the inputs and determine the size of the system
    A = copy(Aa)
    v = copy(va)
    N = len(v)

    # Gaussian elimination
    for m in range(N):

        # Normalization factor
        div = A[up,m]

        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]

        # Now normalize the pivot row of A and subtract from lower ones
        for i in range(up):
            j = m + up - i
            if j<N:
                A[i,j] /= div
                for k in range(1,down+1):
                    A[i+k,j] -= A[up+k,m]*A[i,j]

    # Backsubstitution
    for m in range(N-2,-1,-1):
        for i in range(up):
            j = m + up - i
            if j<N:
                v[m] -= A[i,j]*v[j]

    return v 

def Aamatrix(N):
    aa=zeros([5,N],float)
    aa[2:,0]=array([3,-1,-1],float)
    aa[1:,1]=array([-1,4,-1,-1],float)
    for j in range(2,N-2):
        aa[:,j]=array([-1,-1,4,-1,-1],float)
    aa[:4,N-2]=array([-1,-1,4,-1],float)
    aa[:3,N-1]=array([-1,-1,3],float)
    return aa

def v(N):
    v=zeros(N)
    v[0]=5
    v[1]=5
    return v

N=int(input('number of junctions N='))
v=banded(Aamatrix(N),v(N),2,2)
#print(v)
plot(arange(1,N+1),v)
xlabel('Junction_index')
ylabel('Voltage')
show()



            
    
    