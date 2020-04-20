#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:46:18 2020

@author: juan
"""
#https://www.ugr.es/~lorente/APUNTESMNQ/cap23.pdf

import numpy as np
import matplotlib.pyplot as plt

		
def dx(t,x):
	f = 1/(2*np.pi)
	return np.sin(x*2*np.pi*f)

# def dx(t,x):
#     return np.power(t,2)*x

def kutta(xo,ti,tf):
	h = 0.001 
	t = np.arange(ti,tf,h)
	x = np.zeros(len(t))
	x[0] = xo
	
	for i in range(1,len(t)):
		k_1 = dx(t[i-1],x[i-1])
		k_2 = dx(t[i-1] + (h/2),x[i-1]+(h/2)*k_1)
		k_3 = dx(t[i-1] + (h/2),x[i-1]+(h/2)*k_2)
		k_4 = dx(t[i-1] + h,x[i-1]+h*k_3)
		x[i] = x[i-1] + (h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
		
	return t,x 

iniciales = 100
ti,tf,h = 0,10,0.001
delta = 0.1
t = np.arange(ti,tf,h)
y = np.zeros((iniciales,len(t)))
for i in range(iniciales):
    t,x = kutta(i*delta,ti,tf)
    y[i,:] = x
    plt.plot(t,y[i,:])



# plt.xlim(min(t),max(t))
# plt.plot(t,dx(t,x), label='dx')
# plt.plot(t,x,label='x')
# plt.xlabel('t[s]')
# plt.legend()
# plt.grid()
