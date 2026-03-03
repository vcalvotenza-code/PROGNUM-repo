#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

#integer x values
x = list(range(-5,6)) #x values ranging from -5 to 6

#function
y = []
for value in x:
    y.append(np.cosh(value))

#plot
plt.figure()
plt.plot(x, y, marker='o', label='y = cosh(x)')

plt.title("Catenary curve ", fontsize=12)
plt.xlabel("x values", fontsize=12)
plt.ylabel("y = cosh(x)", fontsize=12)

plt.grid()
plt.legend()

plt.show()


# In[ ]:




