#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, tan, log, log10 
from scipy.integrate import quad

f = input("f(x):")
a = float(input("Input starting value:"))
b = float(input("Input ending value:"))

def d(x, a, b):
    y = eval(f)
    return y

df = quad(d, a, b, args=(a,b))

print(df)

