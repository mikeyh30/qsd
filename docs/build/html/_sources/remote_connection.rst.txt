Interfacing with a Remote Machine
=================================

::

    #!/usr/bin/env python
    from qsd.ssh_control import sshcommand

    # Specify remote computer name
    host = 'monaco'

    sshc = sshcommand.SSHCommand(host,model='cpw_vacuum_calcs.mph',paramfile='paramlist.txt')

    # Securely copy the parameter list to remote machine
    #sshc.scp_params() 

    # Ensure that the remote machine has the folder structure
    sshc.check_host_machine()

    # Copy the parameter file to correct directory
    sshc.set_comsol_data()

    sshc.upload_job_script()

    # Run COMSOL on remote machine
    sshc.run_comsol()

    # Download data from remote machine
    sshc.get_comsol_data()

