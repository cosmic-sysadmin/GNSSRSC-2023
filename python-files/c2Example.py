#Import libraries
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from netCDF4 import Dataset as NCF
import numpy as np
import os
import sys


# Create definitions

def getAtmPrfData(nc): #reads in atmPrf files
    alt = nc.variables['MSL_alt'][:]
    pres = nc.variables['Pres'][:]
    ba = nc.variables['Bend_ang'][:]
    badFile = nc.bad #0 = good, 1 = bad

    return alt, pres, ba, badFile


def getEchPrfData(nc): #reads in echPrf files
    alt = nc.variables['MSL_alt'][:]
    pres = nc.variables['Pres'][:]
    ba = nc.variables['Bend_ang'][:]
    tmp = nc.variables['Temp'][:]

    return alt, pres, ba, tmp


def getWetPf2Data(nc): #reads in wetPrf files
    alt = nc.variables['MSL_alt'][:]
    pres = nc.variables['Pres'][:]
    tmp = nc.variables['Temp'][:]
    badFile = nc.bad #0 = good, 1 = bad

    return alt, pres, tmp, badFile


# Paths to data
dataDir = "/Users/huelsing/Documents/Teaching/Data/"
atmPrfFile = dataDir + "atmPrf_C2E6.2021.168.23.59.G20_0001.0001_nc"
echPrfFile = dataDir + "echPrf_C2E6.2021.168.23.59.G20_0001.0001_nc"
wetPf2File = dataDir + "wetPf2_C2E6.2021.168.23.59.G20_0001.0001_nc"


# Read in data from netCDF files

ncfAtm = NCF(atmPrfFile,'r')
atmAlt, atmPres, atmBa, atmBad = getAtmPrfData(ncfAtm)
ncfAtm.close()

ncfEch = NCF(echPrfFile,'r')
echAlt, echPres, echBa, echTmp = getEchPrfData(ncfEch)
ncfEch.close()

ncfWet = NCF(wetPf2File,'r')
wetAlt, wetPres, wetTmp, wetBad = getWetPf2Data(ncfWet)
ncfWet.close()

# Plot raw profiles

figOutDir = "/Users/huelsing/Documents/Teaching/Graphs/"

titleStr = "Bending Angle on 2021/06/17"
outFile = figOutDir + "BA.png"
fig1 = plt.figure(1, figsize=(9, 6))
grid1 = plt.GridSpec(4, 6, hspace=0.2, wspace=0.5)
ax1  = fig1.add_subplot(grid1[:, :])
ax1.plot(atmBa,atmAlt,linestyle='-',color='black',linewidth=2,label="atmPrf")
ax1.plot(echBa,echAlt,linestyle='-',color='green',linewidth=2,label="echPrf")
ax1.set_xlabel("Bending Angle (radians)",fontsize = 16)
ax1.set_ylabel("Height (km)",fontsize = 16)
# ax1.set_ylim([0,40]) #y-axis limits
# ax1.set_xlim([-0.02,0.02]) #x-axis limits
ax1.tick_params(axis='both', which='major', labelsize=13) #controls axis tick labels
ax1.legend(loc=1, borderaxespad=0.,fontsize = 9) #adds legend
plt.title(titleStr,fontsize = 18,fontweight="bold") #adds plot title
fig1.savefig(outFile, bbox_inches='tight',dpi=300) #where to save plus image quality (dpi)
plt.close(fig1)


titleStr = "Temperature on 2021/06/17"
outFile = figOutDir + "Tmp.png"
fig2 = plt.figure(1, figsize=(9, 6))
grid2 = plt.GridSpec(4, 6, hspace=0.2, wspace=0.5)
ax2  = fig2.add_subplot(grid2[:, :])
ax2.plot(wetTmp,wetAlt,linestyle='-',color='black',linewidth=2,label="wetPf2")
ax2.plot(echTmp,echAlt,linestyle='-',color='green',linewidth=2,label="echPrf")
ax2.set_xlabel("Temperature (deg C)",fontsize = 16)
ax2.set_ylabel("Height (km)",fontsize = 16)
ax2.tick_params(axis='both', which='major', labelsize=13)
# ax2.set_ylim([0,40]) #y-axis limits
# ax2.set_xlim([-0.02,0.02]) #x-axis limits
ax2.legend(loc=1, fontsize = 12)
plt.title(titleStr,fontsize = 18,fontweight="bold") #adds plot title
fig2.savefig(outFile, bbox_inches='tight',dpi=300)
plt.close(fig2)
