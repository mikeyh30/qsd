Postprocessing - Pi Pulse Fidelity
==================================

::


    from scipy import constants as sp
    import os
    import numpy as np
    from matplotlib import pyplot as plt
    from process_data import ReadComsol,PostProcData

    # Read data from downloads
    file_dbx = os.getcwd() + '/data_postprocess/downloads/exports/Bx_fullData.csv'
    file_dby = os.getcwd() + '/data_postprocess/downloads/exports/By_fullData.csv'

    rdx = ReadComsol.ReadComsol(file_dbx)
    rdy = ReadComsol.ReadComsol(file_dby)

    # Read csv file, and get x,y annd dbx/dby data for each
    # blocked point in space
    bx_x,bx_y,bx_z = rdx.read_full_data()
    by_x,by_y,by_z = rdy.read_full_data()

    dbx = np.asarray(bx_z).astype(np.float)
    dby = np.asarray(by_z).astype(np.float)

    # Postprocess data
    post = PostProcData.PostProcData()

    # Calculate total B1 field
    theta = 0
    B1 = post.B1(dbx, dby, theta)

    # Calculate Larmor frequency
    gamma = 4.32e07 # Bismuth gyromagnetic ratio (rad/T*s)
    omega_larmor = post.larmor_omega(B1,gamma)
    tau = 1
    theta_larmor = post.larmor_theta(omega_larmor, tau)

    lardens, laredge = post.larmor_density(bx_x,by_y,theta_larmor)

    # Weight theta with contribution to spin signal
    g_weight = np.zeros(len(laredge))
    for i in range (0,len(laredge)-1):
        g_weight[i] = sum(g[np.where(np.logical_and(theta_larmor>=laredge[i], theta_larmor<=laredge[i+1]))])

    rho_weighted = lardens * g_weight**2

    plt.plot(laredge,rho_weighted)
    plt.show()
