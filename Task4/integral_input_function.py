#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, tan, log, log10 
from scipy.integrate import quad

#boundaries 
a = float(input("Input starting value:"))
b = float(input("Input ending value:"))

#x
x = np.random.uniform(a, b, 1000)
n = len(x)

#formula
f = input("f(x):")

#defining f
def ef(x):
    ef = eval(f)
    return ef
Form = ef(x)

#Monte Carlo aproximation
Sum = 0
for i in range(1,n):
    Sum += Form[i]
    
montecarlo_f = ((b-a)/n)*(Sum)
print("The integral of the inputed formula by Monte Carlo approximation is:",montecarlo_f)

