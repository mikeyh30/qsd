#!python

import os

def add_remote_machine(self):

    file = open("keygen","w")
    file.write("#!/bin/bash")
    file.write("cd ~/.ssh\n")
    file.write("ssh-keygen\n")
    file.write("scp id_rsa %s:/~/.ssh/authorized-keys\n" % self.fullhost)
    file.write("cd -\n")
    file.close()

    file = open(os.getenv("HOME") + '/.ssh/config',"a")

    file.write("\n"
    file.write("Host gade\n")
    file.write("    HostName %s\n" % self.full_host)
    file.write("    User %s\n" % self.user)
    file.write("    IdentityFile ~/.ssh/id_rsa")
    file.close()

