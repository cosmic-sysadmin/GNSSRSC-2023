# Download GNSS data form data.cosmic.ucar.edu

import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import requests
import tarfile
import os
import shutil

global dump

myurl = "https://data.cosmic.ucar.edu/gnss-ro/cosmic2/provisional/spaceWeather/level2/2022/010/ionPrf_prov1_2022_010.tar.gz"

req = requests.get(myurl )

def save_file():
    global dump

with open('/Users/Python-LAB/Ionosphere/IonPrf/ionPrf_prov1_2022_010.tar.gz', 'wb') as myfile:
    myfile.write(req.content)

print(req.encoding)
print(req.headers['content-type'])
print(req.status_code)


target_path = "/Users/Python-LAB/Ionosphere/IonPrf/ionPrf_prov1_2022_010.tar.gz"

data_dir = "/Users/Python-LAB/Ionosphere/IonPrf/ionPrf"

# open file
file = tarfile.open(target_path)
  
# extracting file
file.extractall(data_dir)
  
file.close()




