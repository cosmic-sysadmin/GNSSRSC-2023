#!/usr/bin/env python
# coding: utf-8


# Download GNSS data form data.cosmic.ucar.edu

import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import requests
import tarfile


url = 'https://data.cosmic.ucar.edu/gnss-ro/spire/noaa/nrt/level1b/2023/110/podTec_nrt_2023_110.tar.gz'
target_path = '../GNSS-data/cosmic2/podTc2/podTec_nrt_2023_110.tar.gz'

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(target_path, 'wb') as f:
        f.write(response.raw.read())

data_dir = '../GNSS-data/cosmic2/podTc2/'

# open file
file = tarfile.open(target_path)
  
# extracting file
file.extractall(data_dir)
  
file.close()





