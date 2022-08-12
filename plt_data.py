import warnings
from pathlib import Path
import iris
import math
import iris.cube
import iris.quickplot as qplt
import matplotlib.pyplot as plt
import numpy as np

data_dir_obs = Path.home()/ "WASP_data"
pltname = "Wasp96b_Trans_Data.pdf"

JWST = np.loadtxt(data_dir_obs / f"JWST_data.txt")
Nik = np.loadtxt(data_dir_obs / f"Nikolov_2022_data.txt")

#print(JWST)
#print(Nik)

#Slice JWST data into useable arrays
JWST_wavelengths = JWST[:,0] #Extract wavelength data
Err_JWST_wavelengths = JWST[:,1] #Extract uncertainty in wavelength data
JWST_R_p_over_R_s_sqr = JWST[:,2] # Extract R_p over R_s 
Err_JWST_R_p_over_R_s_sqr = JWST[:,3] # extract uncertainty in R_p over R_s

# Slice Nikolov data
Nik_wavelengths = Nik[:,0]
Err_Nik_wavelengths = Nik[:,1]
Nik_R_p_over_R_s = Nik[:,2]
Err_Nik_R_p_over_R_s = Nik[:,3]

Nik_R_p_over_R_s_sqr = []
Err_Nik_R_p_over_R_s_sqr = []

# Need to square the data in the 3/4 th columns
for i in range(len(Nik_R_p_over_R_s)):
    a = Nik_R_p_over_R_s[i]**2
    Nik_R_p_over_R_s_sqr.append(a)

#Nikolov dataset gives standard deviation of datapoints this is the error from there plots, then multply by 2 and the value of R_p_over_R_s for error propagation
for i in range(len(Err_Nik_R_p_over_R_s)):
    a = 2*Nik_R_p_over_R_s[i]*Err_Nik_R_p_over_R_s[i]
    Err_Nik_R_p_over_R_s_sqr.append(a)

plt.figure(figsize = (15,8))
# Plot JWST data with errorbars
plt.scatter(JWST_wavelengths,JWST_R_p_over_R_s_sqr, color = 'r', label = "JWST data")
plt.errorbar(JWST_wavelengths,JWST_R_p_over_R_s_sqr,xerr = Err_JWST_wavelengths,yerr = Err_JWST_R_p_over_R_s_sqr, fmt = 'o', color = 'r')
# Plot Nikolov 2022 data with errorbars 
plt.scatter(Nik_wavelengths,Nik_R_p_over_R_s_sqr, color = 'b',label = "Nikolov 2022 data")
plt.errorbar(Nik_wavelengths,Nik_R_p_over_R_s_sqr,xerr = Err_Nik_wavelengths,yerr = Err_Nik_R_p_over_R_s_sqr,fmt = 'o',color = 'b')
plt.xlabel("Wavelength [$\mu$m]")
plt.ylabel("($R_p/R_s)^2$")
#plt.xlim()
#plt.ylim()
plt.legend()
#plt.savefig(data_dir/pltname)
plt.show()