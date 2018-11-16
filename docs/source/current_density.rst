Preprocessing - Determine the Current Density 
=============================================

The first thing which is required is to define the geometry of the cpw. In this code exapmle, we call the SetParams object, which reads a text file containing the relevant resonator parameters. We define a grid over the enntire resonator structure, and then calcualte analytically the current density and critical current for the cpw. These values are saved in a parameter listr which gets sent to COMSOL, and the datafiles are stored locally.

::

   import csv
   from vacuum_flucs import CPW
   from process_data import SetParams
   
   # Define geometry of the superconductor
   setp = SetParams.SetParams()
   params = setp.set_params()
   w = params["w"]
   t = params["t"]
   l = params["l"]
   pen = params["pen"]

   # Define resonator params
   omega = params["omega"]
   Z = params["Z"]

   # Define the 'mesh'
   x = np.linspace(-w, w, int(1e04))

   # Instantiate Special CPW object
   cpw = CPW.CPW(x,l,w,t,pen,Z,omega)

   Js = cpw.J() #s Current density - not normalised
   Jnorm = cpw.normalize_J() # Normalise
   I = cpw.current(norm='no') # Find the current

   # Generate a parameter list for COMSOL modelling
   paramlist = setp.param_list(x,I,Jnorm) # Generate COMSOL parameter list

   currentDensityFile = str(os.getcwd() + "/data_preprocess/current_density.csv")
   np.savetxt(currentDensityFile, np.column_stack((x,Jnorm)), delimiter=",")

   currentFile = str(os.getcwd() + "/data_preprocess/current.csv")
   np.savetxt(currentFile, np.column_stack((x,I)), delimiter=",")

