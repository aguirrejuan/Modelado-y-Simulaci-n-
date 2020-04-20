#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:43:41 2020

@author: juan
"""
#https://es.wikipedia.org/wiki/M%C3%A9todo_de_Euler
import numpy as np 
import matplotlib.pyplot as plt 

	
def dx(t,x):
	f = 1/(2*np.pi)
	return np.sin(x*2*np.pi*f)

# def dx(t,x):
#     return np.power(t,2)*x

def euler(xo,ti,tf):
	h =0.001
	t = np.arange(ti,tf,h)
	x = np.zeros(len(t))
	x[0]=xo
	for i in range(1,len(t)):
		x[i]= x[i-1] + h*dx(t[i-1],x[i-1])
		
	return t,x

t,x = euler(0,0,10)

plt.xlim(min(t),max(t))
plt.plot(t,dx(t,x),label='dx')
plt.plot(t,x,label='x')
plt.xlabel('t[s]')
plt.legend()
plt.grid()
plt.show()

