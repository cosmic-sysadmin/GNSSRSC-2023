run your own configurations!
----------------------------
1.   review

     | vi ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml 
     |  change the cycles.

2.   configure your own
     cp ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-ctrl.yaml ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-${your_exp_name}.yaml and vi it.
     configurations: quality control, missions, descending/ascending flag

     | create_experiment.py ${JEDI_SRC}/ewok/experiments/gfs-3dvar-c96-${your_exp_name}.yaml 

3.  let's analyze and compare!

    | cd ${JEDI_ROOT}/plots
