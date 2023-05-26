Login
-----------------
1.   Go to the directory where your “KEY-RSC2023-DA.pem” file is saved. 

     | ssh -XY -i “KEY-RSC2023-DA.pem” $your assigned instance

2.   once log in, type "pwd", 
     
     |/home/ec2-user

     | type "ls",
     | ecflow_server  r2d2-experiments-localhost  setup_skylab.sh  work jedi           setup_modules.sh            spack-stack
3.  cat "setup_modules.sh", copy all loines and paste to your woindow. You will see modules are being loaded. When finished you can "module list" and will see 124 modules loaded.

4.  vi "setup_skylab.sh". You can see some directories we will run our experiments; serve port is set here; virtual environment will be turned on. 
    | source etup_skylab.sh

    | Now we are in a virtual environment. your commang line should start with "venv". type "echo $ECF_PORT", the result should be 2500, which is the port we run ecflow.

Get familiar with ECFLOW
-------------------------

5.  sudo /sbin/service mysqld start
    
    | this is to use the r2d2 database

6.  ecflow_start.sh -p $ECF_PORT

7.  ecflow_ui &
    |it takes 30 - 60 seconds to pop up an UI, user interface window. If yours does not. Let one of us know.
    |once see the UI window, click on the serve icon from the menu on the top, click on the manege server and edit, check if the ip address is correct. Then close.


8.   let's do an experiment!
     | create_experiment.py ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml

9.   vi ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml
     will be explained the details tomorrow

10.   how to check/monitor your experiment?
