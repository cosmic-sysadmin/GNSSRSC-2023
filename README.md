# GNSSRSC-2023

## 2023 GNSS Remote Sensing Colloquium Repository

Git repository for the 2023 GNSS Remote Sensing Colloquium. It contains both Jupyter notebook and Python Lab exercises of the 2023 GNSS Remote Sensing Colloquium. 

- Git Repo: https://git@github.com:cosmic-sysadmin/GNSSRSC-2023.git
- Jupyter notebook files: in jupyter-notebooks directory
- Python files: in python-files directory


## List of contributors
- Iurii Cherniak
- Tyson Hager
- Hannah Huelsing
- Maggie Sleziak-Sallee
- Jeremiah Sjoberg
- Garry Romero
- Jan Weiss
- Irina Zakharenkova
- Hailing Zhang
- Zhen Zeng


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
- palettable
- pyyaml
- netcdf4
- jupyter
- Any other types?
 	

## The Data Files: Main file types we will be working with: 

- [COSMIC-2 podTc2 files ](https://data.cosmic.ucar.edu/gnss-ro/cosmic2/nrt/level1b/)
- [COSMIC-2 atmPrf, wetPrf, echPrf and bfrPrf files ](https://data.cosmic.ucar.edu/gnss-ro/cosmic2/nrt/level2/)
- [SPIRE atmPrf, wetPrf, echPrf and bfrPrf files ](https://data.cosmic.ucar.edu/gnss-ro/spire/nrt/level2/)
- Any other types?


# Decide on a Daterange

- Any particular data range for the Lab exercises?


## Set up

- [ ] VM - Instructions here to access and work with the VM
- Tyson and Gary to update this part


- [ ] Local machine - You can also run the notebooks on your own computer/laptop or a remote cluster
- First install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 
- Please note you may need admin priviledges to install miniconda on your local computer. 

- Then install the main dependencies with
conda install -c conda-forge numpy scipy matplotlib pandas cartopy ggplot pyyaml netcdf4 xarray palettable jupyter ipython pip

- You can also create an environment for this i.e:  
conda create -n myenv gnssrsc

- You might need pip to install any other remaining libraries (in case they do not install with the conda install commands) 

- Next, clone this repository locally with:
- git clone git@github.com:cosmic-sysadmin/GNSSRSC-2023.git

- And finally start Jupyter Lab in your home directory: 
jupyter lab
- Inside jupyter lab navigate to notebooks directory to access the colloquium notebooks. You will need internet access to load the data which we will be downloading either from data.cosmic.ucar.edu or will be included in the git repo and will be downloaded at the time of cloning the repository. 


## Reading Recomendations
- [ ] Jupyter Lab [Overview](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)



