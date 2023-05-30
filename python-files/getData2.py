import os
import requests
import tarfile

# specify the data you prefer: mission, filetype, level, ppmode, yr, doy
#mission='spire/noaa'
mission='cosmic2'
ftype = 'atmPrf'
level = 'level2'
ppmod = 'nrt'
yr = '2022'
doy = '110'

fname = ftype+'_'+ppmod+'_'+yr+'_'+doy+'.tar.gz'
url = 'https://data.cosmic.ucar.edu/gnss-ro/'+mission+'/'+ppmod+'/'+level+'/'+yr+'/'+doy+'/'+fname
target_path = mission+'/'+ftype+'/'+fname

dir_list = target_path.split("/")
if not os.path.exists(os.path.dirname(target_path)):
	os.makedirs(os.path.dirname(target_path))

# download the data 
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(target_path, 'wb') as f:
        f.write(response.raw.read())

# open file
file = tarfile.open(target_path)
  
# extracting file
file.extractall(os.path.dirname(target_path))
  
file.close()

# remove .tar.gz file
if os.path.exists(target_path):
	os.remove(target_path)
else:
	print("File does not exist.")
