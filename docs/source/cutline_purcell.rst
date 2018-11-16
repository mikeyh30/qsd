Postprocessing - Purcell Enhancement for a Cut Line
===================================================

::

   #!/usr/bin/env python
   from process_data import ReadComsol,PostProcData
   import numpy as np
   from scipy import constants as sp

   #read in 1d data from comsol for plotting
   bx = ReadComsol.ReadComsol('comsol_datafiles/Bx.csv')
   by = ReadComsol.ReadComsol('comsol_datafiles/By.csv')
   bn = ReadComsol.ReadComsol('comsol_datafiles/normB.csv')

   xx,Bx = bx.read_1D_comsol_data()
   xy,By = by.read_1D_comsol_data()
   xn,Bn = bn.read_1D_comsol_data()

   lambda_c = 6e-03 # Will work out properly, but just testing for now
   epsilon_r = 11.9
   n = np.sqrt(epsilon_r) / sp.c # Dielectric constant
   Q = 20000 # Will get this data from CST
   F = pp.purcell_factor(lambda_c,n,Q)
