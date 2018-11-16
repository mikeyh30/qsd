Interfacing with a Remote Machine
=================================

::

    #!/usr/bin/env python
    from ssh_command import SSHCommand

    sshc = SSHCommand.SSHCommand()

    # Securely copy the parameter list to remote machine
    sshc.scp_params() 

    # Copy the parameter file to correct directory
    sshc.set_comsol_data()

    # Run COMSOL on remote machine
    sshc.run_comsol()

    # Download data from remote machine
    sshc.get_comsol_data()  
