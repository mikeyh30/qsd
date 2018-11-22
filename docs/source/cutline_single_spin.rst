Postprocessing - Single Spin Coupling for a Cut Line
====================================================

::

    from qsd.data_processing import readcomsol,postproc
    import numpy as np
    import os

    #read in 1d data from comsol for plotting
    bx = readcomsol.ReadComsol(os.getcwd() + '/downloads/exports/Bx.csv')
    by = readcomsol.ReadComsol(os.getcwd() + '/downloads/exports/By.csv')
    bn = readcomsol.ReadComsol(os.getcwd() + '/downloads/exports/normB.csv')

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

    #calcualte single spin couplinng coefficient
    pp = postproc.PostProc(w,t,l,pen,omega,Z)
    g = pp.cut_line_single_spin_coupling(Bx,By)

    rho = pp.cut_line_spin_density(g)
    rho = rho / sum(rho)
