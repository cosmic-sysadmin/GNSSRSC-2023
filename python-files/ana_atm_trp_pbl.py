import os
import glob
import xarray as xr
import sys

# # Input the data
# Searching for all netcdf under a directory
f_path = os.path.join('../spire/atmPrf', '*_nc')

# Specify the attribute names you want to extract
attrs = ['fileStamp', 'bad', 'lon', 'lat', 'trtwmo', 'trhwmo', 'balmax', 'zbalmax', 'dnmin', 'zdnmin', 'minh']

# initialize empty dictionary to store output parameters
atm_attrs = {'fileStamp':[], 'bad':[], 'lon':[], 'lat':[], 'trtwmo':[], 'trhwmo':[], 'balmax':[], 'zbalmax':[], 'dnmin':[], 'zdnmin':[], 'minh':[]}

for fname in glob.glob(f_path):
# open the netcdf file
    ds = xr.open_dataset(fname)

#    print(ds.dims)
#    print(ds.coords)
#    print(ds.data_vars)
    
    for attr in attrs:
        if attr in ds.attrs:
            atm_attrs[attr].append(ds.attrs[attr])
    alt = ds.MSL_alt.values
    atm_attrs['minh'].append(min(alt))

    ds.close()

 
import pandas as pd
import numpy as np

# convert a dictionary of Lists to a Dataframe
df = pd.DataFrame(atm_attrs)

# remove the "bad" data and assign the outliers with nan
mask = df['bad'] == '0'
da_atm = df[mask]

chkattr = ['trtwmo', 'trhwmo', 'balmax', 'zbalmax', 'dnmin', 'zdnmin']
for chkvar in chkattr:
    da_atm.loc[da_atm[chkvar] <-900, chkvar] = np.nan
    
# # Visualizing the tropopause: A histogram plotting

# make plots
import matplotlib.pyplot as plt

plt.hist(da_atm['trtwmo'], bins=20, edgecolor='black')
plt.xlabel('trtwmo (C)')
plt.ylabel('Frequency')
plt.show()


# # Visualizing the tropopause: Latitudinal dependence

# lat vs. tropopause parameters
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
lat = da_atm['lat']
ax[0].plot(da_atm['lat'], da_atm['trtwmo']+273.15, 'o', markersize=2)
ax[0].set_xlabel('Latitude')
ax[0].set_ylabel('trtwmo (K)')
ax[0].set_xticks(range(-90,91,30))

ax[1].plot(da_atm['lat'], da_atm['trhwmo'], 'o', markersize=2)
ax[1].set_xlabel('Latitude')
ax[1].set_ylabel('trhwmo (km)')
ax[1].set_xticks(range(-90,91,30))
plt.show()


# # Examination of RO distributions

# global distribution of occ samples 
import cartopy.crs as ccrs
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1, projection=ccrs.Robinson())
ax.set_global()
ax.coastlines()
ax.plot(da_atm['lon'], da_atm['lat'], 'o', markersize=2, transform=ccrs.PlateCarree())
plt.show()


# # Investigation of the PBL

plt.scatter(da_atm['zdnmin'], da_atm['zbalmax'], s=5)
plt.plot([0,10], [0,10], 'r--')
plt.xlabel('PBLH_dnmin (km)')
plt.ylabel('PBLH_balmax (km)')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


# demonstration of the global PBL 

# import the topography data 
dtopo = xr.open_dataset('ETOPO2v2c_f4.nc')
print(dtopo.variables)

'''
fig = plt.figure(figsize=(10,5))
plt.contourf(dtopo.x[:], dtopo.y[:], dtopo.z[:,:]/1000, cmap='viridis')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar()
plt.show()
'''

zi = dtopo.z.sel(x=da_atm['lon'], y=da_atm['lat'], method='nearest')
num = len(da_atm)
topos = np.zeros(num)
for i in range(0, num):
    topos[i] = zi[i,i]/1000

dtopo.close()

# set the topo data into nonnegative 
topos[topos < 0] = 0


import plotly.express as px
import plotly.data as data

# constrain minh below 0.5 km 
indx = (da_atm['minh']-topos) < 0.5

da_atm = da_atm[indx]
topos = topos[indx]

cols = da_atm.zdnmin-topos

fig = px.scatter_geo(da_atm, lat = 'lat', lon='lon', color=cols, color_continuous_scale='Viridis', projection = 'natural earth')
fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
fig.update_traces(marker=dict(size=5), opacity=0.8)
fig.show()

