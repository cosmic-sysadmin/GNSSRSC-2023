import netCDF4
import numpy as np
import matplotlib.pyplot as plt
f = netCDF4.Dataset('/Users/Python-LAB/Ionosphere/IonPrf/ionPrf_C2E3.2022.120.09.42.G29_0001.0001_nc')
print(f.variables.keys()) # get all variable names

for d in f.dimensions.items():
  print(d)
input

lm=int(10)

h = f.variables['MSL_alt'] # height variable
ne = f.variables['ELEC_dens'] # density variable



sz = int(422)

scale=sz-lm

hight = h[lm:sz] 
dens = ne[lm:sz]
#ampl = snr[lm:sz]
#elangl = elev[lm:sz]

#time = t[1:24450]
#power = snr[1:24450]
#phase = phs[1:24450]

f1 = open('/Users/Python-LAB/Ionosphere/IonPrf/ne', 'w')
for i in range(lm,scale):
    print((hight[i] ), (dens[i] ), file=f1)
    
    
f1.close()



plt.plot(dens, hight, linewidth=2)

plt.title('ionPrf_C2E3.2022.120.09.42.G29')
plt.xlabel('Ne, cm-3')
plt.ylabel('h, km')

plt.savefig('/Users/Python-LAB/Ionosphere/IonPrf/ionPrf_C2E3.2022.120.09.42.G29.png')


