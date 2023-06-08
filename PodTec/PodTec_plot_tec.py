import netCDF4
from netCDF4 import Dataset as NCF
import numpy as np
import matplotlib.pyplot as plt

dataDir = "./Data/"

fName = "podTc2_C2E3.2021.020.23.47.0010.R21.02_0001.0001_nc"
tecFile = dataDir + fName

# Filename
fileType = fName[0:6]
const = fName[6:7]
fmNum = fName[7:11]
fYear = fName[12:16]
fDoy = fName[17:20]
fMin = fName[21:23]
fSec = fName[24:26]
timeStr = fName[21:26]
leo = fName[32:35]

f = NCF(tecFile,'r')

for d in f.dimensions.items():
  print(d)
input

print(f.variables.keys()) # get all variable names

d = (f.__dict__['duration'])

lm=int(1)

t = f.variables['time'] # time variable
tec = f.variables['TEC'] # tec variable
snr = f.variables['caL1_SNR'] # height variable
elev = f.variables['elevation'] # elevation variable
s4i = f.variables['S4'] # elevation variable

sz = int(d)

scale=sz-lm

time = t[lm:sz] #+35019
atec = tec[lm:sz]
ampl = snr[lm:sz]
elangl = elev[lm:sz]
scint = s4i[lm:sz]

f.close()

figOutDir = "./Graphs/"

outFile = figOutDir + fileType + "." + fmNum +"."+ leo +"." + fYear + "." + fDoy + "." + fMin +"."+ fSec +".png"

titleStr = ('COSMIC-2' + "    " + fileType + "." + fmNum +"."+ leo +"." + fYear + "." + fDoy + "." + fMin +"."+ fSec)

fig2 = plt.figure(1, figsize=(9, 6))
grid2 = plt.GridSpec(4, 6, hspace=0.2, wspace=0.5)
ax2  = fig2.add_subplot(grid2[:, :])
ax3 = ax2.twinx()
#ax3.set_ylim(-100, 100);

ax2.plot(time, atec, linestyle='-',color='red',linewidth=2, label="COSMIC-2 podTec")
ax3.plot(time, elangl, linestyle='-',color='blue',linewidth=2,label="COSMIC-2 elevation")

ax2.set_xlabel("Time, s",fontsize = 14)
ax2.set_ylabel("TEC (TECU)",fontsize = 14)
ax3.set_ylabel("Elevation (deg)",fontsize = 14)

ax2.tick_params(axis='both', which='major', labelsize=13) #  tick labels
ax2.legend(loc=8, borderaxespad=0.,fontsize = 9) #adds legend
ax3.legend(loc=9, borderaxespad=0.,fontsize = 9) #adds legend
plt.title(titleStr,fontsize = 14) #adds plot title

fig2.savefig(outFile, bbox_inches='tight',dpi=300) # image resolution
plt.close(fig2)



