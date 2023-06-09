Run your own configurations!
----------------------------
1.   Review

     | vi ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml 
     |  echo $ JEDI_SRC    # if not sure the location.

     | change the cycles: lines 15 &16
     | create_experiments.py ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml



2.   Plotting with NCL (NCAR Command Lauguage)

     |  https://www.ncl.ucar.edu/
     |  cd /home/ec2-user/work/JEDI_ROOT/plots
     |  vi plot_fit2gnssro_omb_oma_ctrl.ncl

     | Note: 
     |    -- ncl here uses virtual environment. If you are on the ecflow "venv" window, you need to  type "deactivate" and then type "usencl". To be simple, you can open two terminal windows, one for ecflow and one for plotting. Just use the ssh command to open another window. type "quitncl" to quit ncl.
     | 
     | ncl plot_fit2gnssro_omb_oma_ctrl.ncl


3.   Configure your own
     
     | ls  ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-*yaml

     | Note: 
     |  -- There are a few of configuration files/yamls. Chose one or more to run. Or you can configue your own if you have some ideas on what you want to see.
     | 
     | Make your own (optional):
     cp ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-${your_exp_name}.yaml and "vi" it.

     |    Configurations: quality control, missions, descending/ascending flag, etc.

     | create_experiment.py ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-${your_exp_name}.yaml 

4.  Analyzing and comparing!

    | cd ${JEDI_ROOT}/plots
    | Refer to the  introduction slides given on FRIDAY. 
