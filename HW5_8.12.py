# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:48:52 2017

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

G=6.6738e-11
M=1.9891e30
m=5.9722e24
r0=1.471e11
vy0=3.0287e4

def f(r,t):
    [x,y]=r
    ax=-G*M*x*(x**2+y**2)**(-1.5)
    ay=-G*M*y*(x**2+y**2)**(-1.5)
    return np.array([ax,ay],float)

t0=0
h=3600
t1=50000*h

tpoints=np.arange(t0,t1,h)
rpoints=[]
vpoints=[]
vhalfpoints=[]

r=np.array([r0,0],float)
v=np.array([0,vy0],float)
v_half=v+0.5*h*f(r,0)
for t in tpoints:
    rpoints.append([r[0],r[1]])
    vpoints.append([v[0],v[1]])
    vhalfpoints.append([v_half[0],v_half[1]])
    r+=h*v_half
    k=h*f(r,t+h)
    v=v_half+0.5*k
    v_half+=k

rr=np.array(rpoints)
vv=np.array(vpoints)   
plt.subplot(121) 
plt.plot(rr[:,0],rr[:,1])



potential=-G*M*m*(rr[:,0]**2+rr[:,1]**2)**(-0.5)
kinetic=0.5*m*(vv[:,0]**2+vv[:,1]**2)
energy=potential+kinetic
plt.subplot(122)
fig1,=plt.plot(tpoints,energy,label='energy')
fig2,=plt.plot(tpoints,potential,label='potential')
fig3,=plt.plot(tpoints,kinetic,label='kinetic')
plt.legend(handles=[fig1, fig2, fig3])
                                     
plt.show()
