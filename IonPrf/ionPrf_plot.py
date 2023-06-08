#Import libraries
import matplotlib
import matplotlib.pyplot as plt
from netCDF4 import Dataset as NCF
import numpy as np
import os
import requests
import sys
import tarfile

# datapath
dataDir = "./Data/"

# Create definitions
def read_ion_data(nc): #reads in ionPrf
    alt = nc.variables['MSL_alt'][:] #altitude, km
    ed = nc.variables['ELEC_dens'][:] #plasma density, n
    
    return alt, ed  #altitude, density

fName = "ionPrf_C2E1.2022.010.19.32.G14_0001.0001_nc"
ionFile = dataDir + fName

# Filename
fileType = fName[0:6]
const = fName[6:7]
fmNum = fName[7:11]
fYear = fName[12:16]
fDoy = fName[17:20]
fMin = fName[21:23]
fSec = fName[24:26]
timeStr = fName[21:26]
leo = fName[27:30]

# Read netCDF
ncfIon = NCF(ionFile,'r')
ionAlt, ionEd = read_ion_data(ncfIon)
ncfIon.close()

# Plot EDP profile
figOutDir = "./Graphs/"
outFile = figOutDir + fileType + "." + fmNum +"."+ leo +"." + fYear + "." + fDoy + "." + fMin +"."+ fSec +".png"

titleStr = ('COSMIC-2 EDP' + "    " + fileType + "." + fmNum +"."+ leo +"." + fYear + "." + fDoy + "." + fMin +"."+ fSec)

fig1 = plt.figure(1, figsize=(9, 6))
grid1 = plt.GridSpec(4, 6, hspace=0.2, wspace=0.5)
ax1  = fig1.add_subplot(grid1[:, :])
ax1.plot(ionEd,ionAlt,linestyle='-',color='red',linewidth=2,label="COSMIC-2 ionPrf")
ax1.set_xlabel("Electron Density (el/cm^3)",fontsize = 14)
ax1.set_ylabel("Height (km)",fontsize = 14)
ax1.set_ylim([50,600]) #y-axis limits
#ax1.set_xlim([-100000,1000000]) #x-axis limits
ax1.tick_params(axis='both', which='major', labelsize=12) # tick labels
ax1.legend(loc=1, borderaxespad=0.,fontsize = 9) # legend
plt.title(titleStr,fontsize = 14) # plot title

fig1.savefig(outFile, bbox_inches='tight',dpi=300) #image quality (dpi)
plt.close(fig1)
