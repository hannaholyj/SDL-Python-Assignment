#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
#1. parsing and storing data - wavelength and flux 
def parse_data(filename):
    wavelength = []
    flux = [] #defining stores fro extracted data 
    with open(filename, 'r') as file:
        for line in file.readlines()[27:]: #first 27 rows are headers/not wavelength and flux
            data = line.strip().split(",") # splitting wavelength and flux 
            wavelength.append(float(data[0]))
            flux.append(float(data[1]))
    return wavelength, flux 
wavelength, flux = parse_data(args.filename)
# print(wavelength,flux) check in terminal 
plt.title("Plot of Full Spectrum")
plt.xlabel("Wavelength (Å)")
plt.ylabel("flux (ADU)")
plt.grid(True)
plt.plot(wavelength,flux) #visualising data
plt.show()


# In[60]:


#2. Fit a low-order polynomial to the background, Fit a Gaussian to the peak and Extract all the relevant parameters (and uncertainties) 
def polynomial(x, a, b, c): #defining polynomial function
    return a*x**2 + b*x + c

#excluding data inside the peak region - background (6680 - 6690 A)
background = (np.array(wavelength) < 6680) | (np.array(wavelength) > 6695)
#fitting points (background only)
p, cov = curve_fit(polynomial, np.array(wavelength)[background], np.array(flux)[background])
#inspect
plt.title("Plot of Spectrum with Fitted Polynomial")
plt.xlabel("Wavelength (Å)")
plt.ylabel("flux (ADU)")
plt.grid(True)
plt.scatter(wavelength,flux, label="Data", s=1) #visualising data
plt.plot(wavelength, polynomial(np.array(wavelength), *p), color='red',label='Fitted polynomial')
plt.legend()
plt.show()


# In[70]:


#defining gaussian function 
def gauss(x, A, mu, sig): #polynomial from above used as curve_fit failed to fit all parameters otherwise
    return polynomial(x,*p) + (A*np.exp(-((x-mu)**2)/(2*sig**2)))
#defining 'peak' region 
peak = (np.array(wavelength) > 6680) & (np.array(wavelength) < 6695)
#initial guess - amplitude, centre of peak and sigma - by eye
p0 = [60, 6685, 2]
p1, cov1 = curve_fit(gauss, np.array(wavelength)[peak], np.array(flux)[peak], p0=p0)
#print(p1,cov1)


# In[58]:


plt.title("Plot of Spectrum with Fitted Gaussian")
plt.xlabel("Wavelength (Å)")
plt.ylabel("flux (ADU)")
plt.grid(True)
plt.scatter(wavelength,flux, label="Data", s=1) #visualising data
plt.plot(wavelength,gauss(np.array(wavelength), *p1), color='red',label='Fitted gaussian')
plt.legend()
plt.show()


# In[56]:


plt.title("Plot of Spectrum with Fitted Gaussian and Polynomial")
plt.xlabel("Wavelength (Å)")
plt.ylabel("flux (ADU)")
plt.grid(True)
plt.scatter(wavelength,flux, label="Data",s=1) #visualising data
plt.plot(wavelength,gauss(np.array(wavelength), *p1), color='red',label='Fitted gaussian')
plt.plot(wavelength, polynomial(np.array(wavelength), *p), color='black',label='Fitted polynomial', linestyle='--')
plt.legend()
plt.show()


# In[48]:


#extracting uncertainties 
#polynomial 
sig_p = np.sqrt(np.diag(cov))
print("Uncertainty on a is:",sig_p[0], "Uncertainty on b is:", sig_p[1], "Unceratinty on c is:", sig_p[2])


# In[68]:


#gaussian 
sig_gaus = np.sqrt(np.diag(cov1))


# In[69]:


#FWHM
FWHM = 2.355*p1[2]
FWHM_sig = 2.355*sig_gaus[2]
print("The FWHM is:", FWHM,"±", FWHM_sig,"Å")
print("The Amplitude: " ,p1[0], "±", sig_gaus[0], "ADU")
print("The central wavelength:", p1[1], "±", sig_gaus[1], "Å")


# In[ ]:




