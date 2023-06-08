import netCDF4
from netCDF4 import Dataset as NCF
import numpy as np

dataDir = "./Data/"

fName = "podTc2_C2E2.2021.020.17.14.0027.R18.01_0001.0001_nc"
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
snr1 = f.variables['caL1_SNR'] # snr variable
elev = f.variables['elevation'] # elevation variable
s4i = f.variables['S4'] # S4 variable

sz = int(d)

scale=int(sz-20)

time = t[lm:sz] #+35019
atec = tec[lm:sz]
l1snr = snr1[lm:sz]
l2snr = snr1[lm:sz]
elangl = elev[lm:sz]
scint = s4i[lm:sz]

f.close()

tectxt = dataDir + fileType + "." + fmNum +"."+ leo +"." + fYear + "." + fDoy + "." + fMin +"."+ fSec +".txt"

f1 = open(tectxt, 'w')
for i in range(lm,scale):
    print((time[i] ), (" "), round((atec[i] ),3), (" "), round((elangl[i] ),3), (" "), round((l1snr[i] ),3), (" "), (scint[i] ), file=f1)
f1.close()


