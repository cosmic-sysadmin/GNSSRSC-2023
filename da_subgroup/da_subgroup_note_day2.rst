Login
-----------------
1.  Go to the directory where your “KEY-RSC2023-DA.pem” file is saved. 

    | ssh -XY -i “KEY-RSC2023-DA.pem” $your assigned instance
    | NOTE: the entire command is included in the email from me (subject: "AWS instance login"). 


2.   Once log in, type "pwd", 
     
     | /home/ec2-user

     | type "ls",
     | ecflow_server  r2d2-experiments-localhost  setup_skylab.sh  work jedi           setup_modules.sh            spack-stack
3.  "source setup_modules.sh".  When finished you can "module list" and will see 124 modules loaded.

4.  "vi setup_skylab.sh". You can see some directories where we will run our experiments; server port is set here; virtual environment will be turned on. 

    | source setup_skylab.sh
    |
    | Now we are in a virtual environment. Your command prompt should start with "venv". Type "echo $ECF_PORT", the result should be 2500, which is the port we run ecflow.

Get familiar with ECFLOW
-------------------------

5.  sudo /sbin/service mysqld start
    
    | This is to use the r2d2 database

6.  ecflow_start.sh -p $ECF_PORT
    | This command will generate screen messages. Pay attention to the last three lines. You will see your "host name" which is your instance's IP address.

7.  ecflow_ui &

    | It takes 30 - 60 seconds to pop up an UI, the user interface window. If yours does not, Let one of us know (Hailing or hsiao-Chun).
    | Once you see the UI window, click on the server icon from the menu on the top, click on the manege server and edit, check if the ip address is correct. Then close. 
    | NOTE: you can change the host name to whatever you like. You may need to close the UI window and re-type "ecflow_UI" to reflect the change.
    | NOTE: this step needs to be done only once.


8.  Let's do an experiment!

    | create_experiment.py ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml
    | NOTE: echo $JEDI_SRC to check the directory.

9.  vi ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml

    |  will be explained the details tomorrow.


10. Check/monitor your experiment? 
     
    |  ecflow_ui  
    | /home/ec2-user/work/JEDI_ROOT/workdir
