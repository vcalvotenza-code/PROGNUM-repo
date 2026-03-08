#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Defining one dimensional gaussian formula
def gauss(x, A, x0, sigma, z0):
    return A * np.exp(-(x - x0)**2 / (2 * sigma**2)) + z0

# Getting user inputs
A = float(input("Enter amplitude A: "))
x0 = float(input("Enter peak position x0: "))
sigma = float(input("Enter width sigma: "))
z0 = float(input("Enter z0 (offset in y): "))
a = float(input("Enter lower integration limit: "))
b = float(input("Enter upper integration limit: "))

# Calculating the area from a and b inputs
area, error = quad(gauss, a, b, args=(A, x0, sigma, z0))
print(f"Area between {a} and {b}: {area:.3f} (error: {error:.2e})")

# Calculate total area with infinity and with the second formula givn
area_total, error_total = quad(gauss, -np.inf, np.inf, args=(A, x0, sig, z0))
area_f_2 = A * sig * np.sqrt(2 * np.pi)
print(f"Total area (-inf., inf.): {area_total:.3f}")
print(f"Total area (simplyfies formula): {area_f_2:.3f}")

# Expanded x range for plotting
x_min = min(-10, a - 2)                                     # -2 and +2 to make more space 
x_max = max(10, b + 2)
x_plot = np.linspace(x_min, x_max, 200)   
y_plot = gauss(x_plot, A, x0, sigma, z0)                    # Using agains the gauss formula for the y plot

# Creating the plot 
plt.figure(figsize=(10, 6))                                 # Looking of the graph

# Plotting the full Gaussian
plt.plot(x_plot, y_plot, color='blue', linewidth=2,
         label=f'Gaussian: A={A}, x0={x0}, sigma={sigma}, z0={z0}')

# Creating x values for the shaded region and filling the area under the curve
x_fill = np.linspace(a, b)                                  # from a to b 
y_fill = gauss(x_fill, A, x0, sig, z0)                      # Using gaussian formula with the other parameters + the x_fill parameter
plt.fill_between(x_fill, y_fill, 0, alpha=0.3, color='red',
                 label=f'Area [{a:.2f}, {b:.2f}] = {area:.4f}')  # Using plt.fill_between again for the shaded area

# Adding vertical lines for integration limits
plt.axvline(x=a, color='red', linestyle='--', alpha=0.7, linewidth=1)
plt.axvline(x=b, color='red', linestyle='--', alpha=0.7, linewidth=1)

# Adding labels and more details
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Area Under a Gaussian Curve (Interactive Parameters)')
plt.grid(True)
plt.legend()
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)

# Adding info box with parameters
param_text = f'A={A}, x_0={x0}, sigma={sig}, z_0={z0}// Total area = {area_total:.4f}'
plt.text(-10, 0.6, f'A={A}, x_0={x0}, sigma={sig}, z_0={z0}\nTotal area = {area_total:.4f}')

plt.show()


# ![gaussian distribution.png](attachment:1de04449-a562-4ff8-b5d7-39bba3aea6ce.png)

# In[ ]:




