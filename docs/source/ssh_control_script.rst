ssh_control
===========

This package contains a script which calls bash scripts, which interface with a remote machine

get_comsol_data
^^^^^^^^^^^^^^^

::

   #!/bin/sh
   # This bash script logs into the remote machine where the COMSOL calculations were performed, and downloads the required datafiles into the data_postprocessing directory

    HOST="gade"
    #REMOTEDIR="/homes/gjones/COMSOL_files/output"
    REMOTEDIR="COMSOL_files/exports"
    DOWNLOADDIR="./data_postprocess/downloads"
    scp -r ${HOST}:${REMOTEDIR} ${DOWNLOADDIR}

set_comsol_data
^^^^^^^^^^^^^^^

::

    #!/bin/bash
    # This bash file securely copies a parameter file to the remote machine which hosts the COMSOL module. The parameterlist file is renamed here to what we will call the COMSOL model onn the remote machine. I need to redo this to make it a bnit more general, as right now I require a login to gade.

    MODELNAME="cpw_vacuum_calcs.mph"
    DIR="./data_preprocess"
    PARAMFILE="${DIR}/${MODELNAME}.txt"
    cp "${DIR}/paramlist.txt" ${PARAMFILE}
    scp ${PARAMFILE} gade:/homes/gjones/COMSOL_files/parameter_files
    rm ${PARAMFILE}

run_comsol
^^^^^^^^^^

::

    #!/bin/bash

    HOST=gade # remote computer

    echo "Running COMSOL on ${HOST}"
    ssh ${HOST} 'cd COMSOL_files && ./job input/cpw_vacuum_calcs.mph'; exit

get_comsol_data
^^^^^^^^^^^^^^^

::

    #!/bin/sh
    # This bash script logs into the remote machine where the COMSOL calculations were performed, and downloads the required datafiles into the data_postprocessing directory

    HOST="gade"
    #REMOTEDIR="/homes/gjones/COMSOL_files/output"
    REMOTEDIR="COMSOL_files/exports"
    DOWNLOADDIR="./data_postprocess/downloads"
    scp -r ${HOST}:${REMOTEDIR} ${DOWNLOADDIR}
