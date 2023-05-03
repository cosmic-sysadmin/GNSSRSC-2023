# GNSSRSC-2023

-



## 2023 GNSS Remote Sensing Colloquium 

This repository contains Jupyter notebooks for the lab exerc of the 2023 GNSS Remote Sensing Colloquium lab exercises


## List of contributors

Add list of people that have contributed to these repository (craeted Jupyter labs, set up instructions)

## Lab exercises

List of Jupyter books available to work with for the Colloquium labs

## Requirements
The jupyter notebooks require the following Python libraries: 
- numpy
- pip
- scipy
- matplotlib
- cartopy
- pandas
- ggplot
- xarray
- libnetcdf
- palettable
- pyyaml
- netcdf4
- jupyter
- (Please add as need) 	


## The Data Files: Main file types we will be working with: 

- [ ] [COSMIC-2 podTc2 files ](https://data.cosmic.ucar.edu/gnss-ro/cosmic2/nrt/level1b/2023/115/)
- [ ] [COSMIC-2 atmPrf, wetPrf, echPrf and bfrPrf files ](https://data.cosmic.ucar.edu/gnss-ro/cosmic2/nrt/level2/2023/115/)
- [ ] [SPIRE atmPrf, wetPrf, echPrf and bfrPrf files ](https://data.cosmic.ucar.edu/gnss-ro/spire/nrt/level2/2023/115/)
- Let's list any other files types (i.e: ionPrf)


# Decide on a Daterange

- We will need to decide on a daterange for data to use for the lab exercises


## Set up

- [ ] VM - Instructions here to access and work with the VM

- [ ] Local machine - You can also run the notebooks on your own computer/laptop or a remote cluster (provided you have admin privileges to install miniconda on your system)  
- First install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 

- Then install the main dependencies with
conda install -c conda-forge numpy scipy matplotlib pandas cartopy ggplot pyyaml netcdf4 xarray libnetcdf palettable seaborn jupyter ipython pip

- You can also create an environment for this i.e:  
conda create -n myenv gnssrc

- You might need pip to install any other remaining libraries (in case they do not install with the conda install commands) 

- Next, clone this repository locally with:
- git clone https://git.cosmic.ucar.edu/maggie/gnssrsc-2023.git

- And finally start Jupyter Lab in your home directory: 
jupyter lab
- Inside jupyter lab navigate to notebooks directory to access the colloquium notebooks. You will need internet access to load the data which we will be downloading either from data.cosmic.ucar.edu or will be included in the git repo and will be downloaded at the time of cloning the repository. 


## Reading Recomendations
- [ ] Jupyter Lab [Overview](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)

## Additional Notes: 


