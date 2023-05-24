# GNSSRSC-2023

## 2023 GNSS Remote Sensing Colloquium Repository

Git repository for the 2023 GNSS Remote Sensing Colloquium. It contains both Jupyter notebook and Python Lab exercises of the 2023 GNSS Remote Sensing Colloquium. 

- Git Repo: [https://git@github.com:cosmic-sysadmin/GNSSRSC-2023.git](https://github.com/cosmic-sysadmin/GNSSRSC-2023)
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
- [COSMIC-2 ionPrf files ](https://data.cosmic.ucar.edu/gnss-ro/cosmic2/provisional/spaceWeather/level2/)
- [COSMIC-2 atmPrf, wetPrf, echPrf and bfrPrf files ](https://data.cosmic.ucar.edu/gnss-ro/cosmic2/nrt/level2/)
- [SPIRE atmPrf, wetPrf, echPrf and bfrPrf files ](https://data.cosmic.ucar.edu/gnss-ro/spire/nrt/level2/)
- Any other types?


## Decide on a Daterange

- Any particular data range for the Lab exercises?


## Set up

- [ ] VM - Instructions here to access and work with the VM
- Connect to the gnss-rsc-2023 VM via SSH:
	- `Substitute "username" and "password" for the user name and password provided to you`
	- ssh username@128.117.233.100
	- Password: password

Your environment should already be all set up for running the excercises.  Please speak to Gary Romero for any issues encountered.


- [ ] Local machine - You can also run the notebooks on your own computer/laptop or a remote cluster
- First install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 
  - Windows OS: When installing, you can install for just a single user without Admin privileges.
  - MacOS: Depending on configuration, you might need Admin privileges.
  - Note, when installing conda - you can choose "change installation location" and pick "install only for the current user"

- Install the main dependencies. It is recommended that these are installed individually to prevent conflicts during install.

```bash
Optional: 
conda init bash # Or zsh - This puts the path to the configuration for conda in your .bashrc or .zshrc
# You may need to close and reopen your terminal or source the .bashrc

To install the needed libraries: 

conda install -c conda-forge numpy
conda install -c conda-forge scipy
conda install -c conda-forge matplotlib 
conda install -c conda-forge pandas
conda install -c conda-forge cartopy 
conda install -c conda-forge pyyaml
conda install -c conda-forge netcdf4
conda install -c conda-forge xarray
conda install -c conda-forge palettable
conda install -c conda-forge jupyterlab
conda install -c conda-forge pip

If you need another library and conda install cannot find it, you can also use pip
i.e: pip install ggplot
To list all your libraries: conda list or pip list
```

- Create a new directory: i.e.: GNSSRSC-2023

- Next, clone this repository locally with: 
  
  `git clone https://github.com/cosmic-sysadmin/GNSSRSC-2023.git`

- And finally start Jupyter Lab in the git repository directory: 
  `jupyter lab`

- Inside jupyter lab navigate to notebooks directory to access the colloquium notebooks. You will need internet access to load the data which we will be downloading either from data.cosmic.ucar.edu or will be included in the git repo and will be downloaded at the time of cloning the repository. 


- If you would like to create an environment:  
```bash
conda create --name gnssrsc
# navigate to your miniconda3/envs directory
# To activate the environment: 
conda activate gnssrsc
# To deactivate the environment: 
conda deactivate
```

## Reading Recomendations
- [ ] Jupyter Lab [Overview](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)




