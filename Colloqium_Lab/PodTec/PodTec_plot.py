import netCDF4
import numpy as np
import matplotlib.pyplot as plt
f = netCDF4.Dataset('/Users/Python-LAB/Ionosphere/PodTec/podTec_C2E1.2022.318.07.30.0063.G23.00_0001.0001_nc')
print(f.variables.keys()) # get all variable names

for d in f.dimensions.items():
  print(d)
input

lm=int(1)

t = f.variables['time'] # time variable
tec = f.variables['TEC'] # tec variable
snr = f.variables['caL1_SNR'] # height variable
elev = f.variables['elevation'] # elevation variable
sz = int(3797)

scale=sz-lm

time = t[lm:sz] #+35019
atec = tec[lm:sz]
ampl = snr[lm:sz]
elangl = elev[lm:sz]
#scint = S4[lm:sz]
#sigma = SP[lm:sz]

#time = t[1:24450]
#power = snr[1:24450]
#phase = phs[1:24450]

f1 = open('/Users/Python-LAB/Ionosphere/PodTec/tec', 'w')
for i in range(lm,scale):
    print((time[i] ), (atec[i] ), (elangl[i] ), file=f1)
    
    
f1.close()



plt.plot(time, atec, linewidth=2)
plt.plot(time, elangl, linewidth=2)


plt.title('COSMIC-2 - podTec_C2E1.2022.318.07.30.0063.G23')
plt.xlabel('Time, s')
plt.ylabel('aTEC&Elev angl')

plt.savefig('/Users/Python-LAB/Ionosphere/PodTec/podTec_C2E1.2022.318.07.30.0063.G23.png')


