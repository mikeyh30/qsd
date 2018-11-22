Adding a remote machine
=======================

If you want to use ssh protocols to interface with different machines, it is often easier to set up your computers ssh config file such that you have an authenticated connection to a host machine that you recognise. This is achieved by genberating a secure public key which is shared between your machine and the host, and creating an alias so that you can loginn to the remote machine without having to type out the full host name each time. The method 'add_remote_machine' in ssh_control does this for you. Enter the name of the host machine you want to connect to (e.g. monaco/viena/etc) along with the network address and your username, and the rest will be taken care of.

::

    #!/usr/bin/env python

    from qsd import ssh_control

    host_machine = 'monaco'
    network = '.ee.ucl.ac.uk'
    username = 'ucapxxx'

    # Instantiate the ssh object
    sshc = ssh_control.sshcommand()

    # Add the remote machine to you ssh config file in ~.ssh
    sshc.add_remote_machine(host_machine, host_network=network, user=username)
