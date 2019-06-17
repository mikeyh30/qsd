#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import csv
import qsd
import os

# Define geometry of the superconductor
paramfile=open("cpw_parameters.txt","r")
filestring = paramfile.read()
filelist = filestring.split("\n")

pd = {}
for fl in filelist:
    l = fl.split()
    pd[l[0]] = l[2]
paramfile.close()

w = float(pd["w"])
t = float(pd["t"])
l = float(pd["l"])
pen = float(pd["pen"])
omega = float(pd["omega"])
Z = float(pd["Z"])

setp = qsd.data_processing.setparams.SetParams()#w,t,l,pen,omega,Z)
params = setp.set_params("cpw_parameters.txt")

# Define the 'mesh'
x = np.linspace(-w, w, int(1e04))

# Instantiate Special CPW object
cpw = qsd.electromagnetics.CPW(x,l,w,t,pen,Z,omega)

Js = cpw.J() #s Current density - not normalised
Jnorm = cpw.normalize_J() # Normalise 
I = cpw.current(norm='no') # Current
E = cpw.E() # Electric field
sigma = cpw.conductivity() # Conductivity

# Generate a parameter list for COMSOL modelling
paramlist = setp.param_list(x,I,Jnorm,"paramlist.txt") # Generate COMSOL parameter list

# Save data to csv file
currentDensityFile = str(os.getcwd() + "/data_preprocess/current_density.csv")
np.savetxt(currentDensityFile, np.column_stack((x,Jnorm)), delimiter=",")

currentFile = str(os.getcwd() + "/data_preprocess/current.csv")
np.savetxt(currentFile, np.column_stack((x,I)), delimiter=",")

eFile = str(os.getcwd() + "/data_preprocess/electric_field.csv")
np.savetxt(eFile, np.column_stack((x,E)), delimiter=",")

condFile = str(os.getcwd() + "/data_preprocess/conductivity.csv")
np.savetxt(condFile, np.column_stack((x,sigma)), delimiter=",")

# Plot data - can decide to show or not, and save or not
#plts = Plotting.Plotting()

plt0 = plt.plot(x*1e6,I,color = 'b')
plt.xlabel('x ($\mu$m)')
plt.ylabel('$Current (A/m)$')
plt.savefig('current.eps')
plt.show()

#plt1 = plts.plot(x*1e6,Jnorm*1e6,colr='r',xlab='x ($\mu$m)',
#	ylab='Current density\n (MAm$^{-2}$)',
#	filename='current_density.eps',show='no',save='yes')
plt1 = plt.plot(x*1e6,Jnorm*1e6,color = 'r')
plt.xlabel('x ($\mu$m)')
plt.ylabel('Current density\n (MAm$^{-2}$)')
plt.savefig('current_density.eps')
plt.show()

#plt2 = plts.plot(x*1e6,sigma,colr='g',xlab='x ($\mu$m)',
#	ylab='Conductivity\n ($S/m}$)',
#	filename='conductivity.eps',show='no',save='yes')
plt2 = plt.plot(x*1e6,sigma,color = 'g')
plt.xlabel('x ($\mu$m)')
plt.ylabel('Conductivity\n ($S/m}$)')
plt.savefig('conductivity.eps')
plt.show()

#plt3 = plts.plot(x*1e6,E,colr='b',xlab='x ($\mu$m)',
#	ylab='Electric Field\n ($V/m$)',
#	filename='e_files.eps',show='no',save='yes')
plt3 = plt.plot(x*1e6,E,color = 'b')
plt.xlabel('x ($\mu$m)')
plt.ylabel('Electric Field\n ($V/m$)')
plt.savefig('e_files.eps')
plt.show()