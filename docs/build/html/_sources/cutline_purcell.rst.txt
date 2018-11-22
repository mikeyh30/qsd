Postprocessing - Purcell Enhancement for a Cut Line
===================================================

::

    #!/usr/bin/env python
    from qsd.data_processing import readcomsol,postproc
    import numpy as np
    from scipy import constants as sp
    import os

    #read in 1d data from comsol for plotting
    bx = readcomsol.ReadComsol(os.getcwd() + 'downloads/exports/Bx.csv')
    by = readcomsol.ReadComsol(os.getcwd() + 'downloads/exports/By.csv')
    bn = readcomsol.ReadComsol(os.getcwd() + 'downloads/exports/normB.csv')

    xx,Bx = bx.read_1D_comsol_data()
    xy,By = by.read_1D_comsol_data()
    xn,Bn = bn.read_1D_comsol_data()

    # Define geometry of the superconductor
    setp = setparams.SetParams()
    params = setp.set_params("cpw_parameters.txt")

    w = params["w"]
    t = params["t"]
    l = params["l"]
    pen = params["pen"]
    omega = params["omega"]
    Z = params["Z"]

    lambda_c = 6e-03 # Will work out properly, but just testing for now
    epsilon_r = 11.9
    n = np.sqrt(epsilon_r) / sp.c # Dielectric constant
    Q = 20000 # Will get this data from CST
    F = pp.purcell_factor(lambda_c,n,Q)
