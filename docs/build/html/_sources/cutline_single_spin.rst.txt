Postprocessing - Single Spin Coupling for a Cut Line
====================================================

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

   #calcualte single spin couplinng coefficient
   pp = PostProcData.PostProcData()
   g = pp.cut_line_single_spin_coupling(Bx,By)

   rho = pp.cut_line_spin_density(g)
   rho = rho / sum(rho)
