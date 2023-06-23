#Import libraries
#Import libraries
import matplotlib
import matplotlib.pyplot as plt
from netCDF4 import Dataset as NCF
import numpy as np
import os
import requests
import sys
import tarfile

downloadData = False
# Path to data
dataDir = "../Data/"

# Create definitions
def read_atm_data(nc): #reads in atmPrf files
    alt = nc.variables['MSL_alt'][:] #reads in altitude array in km
    ba = nc.variables['Bend_ang'][:] #reads in bending angle array
    badFlag = nc.bad #0 = good, 1 = bad

    return alt, ba, badFlag

if(downloadData == True):
	## Download data
	url = 'https://data.cosmic.ucar.edu/gnss-ro/cosmic2/nrt/level2/2023/060/atmPrf_nrt_2023_060.tar.gz'
	target_path = "../Data/atmPrf_nrt_2023_060.tar.gz"

	response = requests.get(url, stream=True)
	if response.status_code == 200:
	    with open(target_path, 'wb') as f:
	        f.write(response.raw.read())

	# open file
	file = tarfile.open(target_path)
	# extracting file
	file.extractall(dataDir)
	file.close()

# Read in data from netCDF files
# Grab one file
fName = "atmPrf_C2E1.2023.060.01.36.G19_0001.0001_nc"
atmFile = dataDir + fName

# Filename info
fileType = fName[0:6]
const = fName[7:9]
fmNum = fName[10:11]
fYear = fName[12:16]
fDoy = fName[17:20]
fHr = fName[21:23]
fMin = fName[24:26]
timeStr = fName[12:26]

# Read in data from netCDF files
ncfAtm = NCF(atmFile,'r')
atmAlt, atmBa, atmBad = read_atm_data(ncfAtm)
ncfAtm.close()

# Plot raw profiles
figOutDir = "../Graphs/"
outFile = figOutDir + "BA."+timeStr+".png"

titleStr = "Bending Angle on 2023/03/01"
fig1 = plt.figure(1, figsize=(9, 6))
grid1 = plt.GridSpec(4, 6, hspace=0.2, wspace=0.5)
ax1  = fig1.add_subplot(grid1[:, :])
ax1.plot(atmBa,atmAlt,linestyle='-',color='black',linewidth=2,label="COSMIC-2 atmPrf")
ax1.set_xlabel("Bending Angle (radians)",fontsize = 16)
ax1.set_ylabel("Height (km)",fontsize = 16)
ax1.set_ylim([0,40]) #y-axis limits
ax1.set_xlim([-0.001,0.04]) #x-axis limits
ax1.tick_params(axis='both', which='major', labelsize=13) #controls axis tick labels
ax1.legend(loc=1, borderaxespad=0.,fontsize = 9) #adds legend
plt.title(titleStr,fontsize = 18,fontweight="bold") #adds plot title
fig1.savefig(outFile, bbox_inches='tight',dpi=300) #where to save plus image quality (dpi)
plt.close(fig1)
