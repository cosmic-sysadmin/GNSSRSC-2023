import netCDF4
from netCDF4 import Dataset as NCF
import numpy as np

dataDir = "./Data/"

fName = "ionPrf_C2E5.2022.010.00.42.G01_0001.0001_nc"
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
leo = fName[32:35]

f = NCF(ionFile,'r')

for d in f.dimensions.items():
    print(d)
input

print(f.variables.keys()) # get all variable names

d = (f.__dict__['shortlen'])


lm=int(1)

alt = f.variables['MSL_alt'][:] #altitude, km
ed = f.variables['ELEC_dens'][:] #plasma density, n
lat = f.variables['GEO_lat'][:] #latitude
lon = f.variables['GEO_lon'][:] #longitude

sz = int(d)

scale=int(sz-20)

f.close()

netxt = dataDir + fileType + "." + fmNum +"."+ leo +"." + fYear + "." + fDoy + "." + fMin +"."+ fSec +".txt"

f1 = open(netxt, 'w')
for i in range(lm,scale):
    print((alt[i] ), (" "), round((ed[i] ),3), (" "), round((lat[i] ),3), (" "), round((lon[i] ),3), file=f1)
f1.close()


