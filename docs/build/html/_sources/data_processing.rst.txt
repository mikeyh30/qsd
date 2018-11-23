data_processing
===============

preproc
^^^^^^^
.. automodule:: qsd.data_processing.preproc
   :members:

::

    #!/usr/bin/env python
    """
    Method to upload data to remote machine
    """
    from subprocess import call

    class PreProc:
        """
        Preprocessing methods
        """
        def upload_data(self):
            """
            Upload data to remote machine
            """
            rc = call("./upload_data")

setparams
^^^^^^^^^
.. automodule:: qsd.data_processing.setparams
   :members:

::

    #!/usr/bin/env python
    """
    This program sets the parameters required for simulation.
    """

    import numpy as np
    import os
    from subprocess import call

    class SetParams:
        """
            This class allows a user to set the relevant parameters of the cpw. This needs refactorinng, but is sufficient for now.
        """
        def __init__(self):
            """
                Initialize with parameters

                :type w: float
                :param w: width of substrate

                :type t: float
                :param t: thickness of superconductor

                :type l: float
                :param l: length of supercondducting wire

                :type pen: float
                :param pen: penetration depth

                :type omega: float
                :param omega: cavity resonant frequency

                :type Z: float
                :param w: characteristic impedance
            """
            self.w = None
            self.t = None
            self.l = None
            self.pen = None
            self.omega = None
            self.Z = None
            self.N = 2

        def set_params(self,infile):
            """
                Returns simulation parameters as a dictionary
            """
            # Define geometry of the superconductor
            paramfile=open(infile,"r")
            filestring = paramfile.read()
            filelist = filestring.split("\n")

            pd = {}
            for fl in filelist:
                l = fl.split()
                pd[l[0]] = l[2]
            paramfile.close()

            self.w = float(pd["w"])
            self.t = float(pd["t"])
            self.l = float(pd["l"])
            self.pen = float(pd["pen"])
            self.omega = float(pd["omega"])
            self.Z = float(pd["Z"])

            params = {'w':self.w,
                't':self.t,
                'l':self.l,
                'pen':self.pen,
                'omega':self.omega,
                'Z':self.Z
            }
            return params

        def param_list(self,x,I,Jnorm,paramfile):
            """
            Generates a text file which holds the parameters requiured for the COMSOL simulation
            """
            n = [abs(i) for i in x]
            idx = n.index(min(n))

            I0 = I[idx]
            J0 = I0/(2*(self.w+self.t)*self.pen)
            pen_perp = self.pen**2 / (2*self.t)
            C = (0.506*np.sqrt(self.w/(2*pen_perp)))**0.75
            l1 = self.pen*np.sqrt(2*self.pen/pen_perp)
            l2 = 0.774*self.pen**2/pen_perp + 0.5152*pen_perp
            J2overJ1 = (1.008/np.cosh(self.t/self.pen)*np.sqrt(self.w/pen_perp/
                (4*pen_perp/self.pen - 0.08301*self.pen/pen_perp)))
            J1 = Jnorm[idx]
            w_sub = 4*self.w
            h_sub = 25e-06

            f = open(paramfile,'w')
            f.write('w ' + str(self.w) + '[m] width_of_superconductor\n'
               't ' + str(self.t) + '[m] thickness_of_superconductor\n'
               'pen ' + str(self.pen) + '[m] penetration_depth\n'
               'I0 ' + str(I0) + '[A/m] current_at_x=0\n'
               'J0 ' + str(J0) + '[A/m^3] current_density_at_x=0\n'
               'N ' + str(self.N) + '\n'
               'w_sub ' + str(w_sub) + '[m] substrate_width\n'
               'h_sub ' + str(h_sub) + '[m] substrate_height\n'
               'pen_perp ' + str(pen_perp) + '[m] perpendicular_pen_depth\n'
               'C ' + str(C) + ' capacitance\n'
               'l1 ' + str(l1) + '[m]\n'
               'l2 ' + str(l2) + '[m]\n'
               'J2overJ1 ' + str(J2overJ1) + '\n'
               'J1 ' + str(J1) + '[A/m]'
               )

            f.close()

readcomsol
^^^^^^^^^^
.. automodule:: qsd.data_processing.readcomsol
   :members:

::

    #!/usr/bin/env python
    """
        Methods for reading data from COMSOL
    """

    import numpy as np
    import csv
    from subprocess import call

    class ReadComsol:
        """
            ReadComsol contains methods for reading datafiles from COMSOL
        """

        def __init__(self,file):
            """
                Initialize with COMSOL file
            """
            self.file = file

        def read_1D_comsol_data(self):
            """
                Read 1D COMSOL datafiles
            """
            x=[]
            y=[]
            with open(self.file, 'r') as rf:
                reader = csv.reader(rf, delimiter=',')
                for row in reader:
                    x.append(row[0])
                    y.append(row[1])
            x = np.asarray((x),dtype=float)
            y = np.asarray((y),dtype=float)
            return x,y

        def read_2D_comsol_data(self):
            """
                Read 2D COMSOL datafiles
            """
            x=[]
            y=[]
            z=[]
            with open(self.file, 'r') as rf:
                reader = csv.reader(rf, delimiter=',')
                for row in reader:
                    x.append(row[0])
                    y.append(row[1])
                    z.append(row[2])
            x = np.asarray((x),dtype=float)
            y = np.asarray((y),dtype=float)
            z = np.asarray((z),dtype=float)
            return x,y,z

            def read_full_data(self):
            """
                Read full COMSOL datafiles
            """
            x=[]
            y=[]
            z=[]
            with open(self.file, 'r') as rf:
                reader = csv.reader(rf, delimiter=',') 
                for row in reader:
                    x.append(row[0])
                    # Remove header from csv file, if it exists
                    if x[0].split()[0] == '%':
                        x.remove(row[0])
                    else:
                        y.append(row[1])
                        z.append(row[2])
            return x,y,z


postproc
^^^^^^^^

.. automodule:: qsd.data_processing.postproc
   :members:

::


    #!/usr/bin/env python

    """
    This program allows a user to determine certain figures of merit of interest for cpw resonators for quantum spin dynamics.
    """

    import numpy as np
    import numpy.matlib
    from scipy import constants as sp
    from qsd.data_processing import setparams

    class PostProc:
        """
        Contains methods for calculating various figures of merit for cpw
        """
        def __init__(self,w,t,l,pen,omega,Z):
            """
            Initializes resonator structure
            """
            #setp = setparams.SetParams()
            #params = setp.set_params()
            #self.w = params["w"]
            #self.t = params["t"]
            #self.l = params["l"]
            #self.pen = params["pen"]

            #define the resonator - from CST or experiment
            #self.omega = params["omega"]
            #self.Z = params["Z"]
            self.w = w
            self.t = t
            self.l = l
            self.pen = pen
            self.omega = omega
            self.Z = Z

            self.g = None

            self.volume_cell = None

        def B1(self,dbx,dby,theta):
            """
            Calculates total B1 field
            """
            #B1 = np.sqrt(dby**2 + (np.cos(theta)**2)*dbx**2)
            B1 = dbx + dby
            return B1

        def larmor_omega(self,B,gamma):
            """
            Calculates larmor precession frequency
            """
            omega_larmor = gamma * B
            return omega_larmor

        def larmor_theta(self,omega_larmor,tau):
            """
            Calculates angle of larmor precession
            """
            theta_larmor = omega_larmor * tau
            return theta_larmor

        def cut_line_single_spin_coupling(self,Bx,By,*args,**kwargs):
            """
            Calculates the single spin coupling for a given grid area
            """
            theta = kwargs.get('theta',0)
            ang = np.cos(theta)
            ue = sp.physical_constants["Bohr magneton"][0]
            self.g = 0.47 * ue * np.sqrt(By**2 + (ang**2) * Bx**2)
            return self.g/sp.h

        def cut_line_spin_density(self,g):
            """
            Calculates the spin density for cut line section
            """
            self.volume_cell = g * self.t * self.l
            rho =  sp.m_e / self.volume_cell
            return rho

        def distribution(self,x,y,param,*args,**kwargs):
            """
            Method to calculate histogram
            """
            bin_num = kwargs.get('bins',500)
            Ncell = self.ncell(x,y,param)
            param = np.matlib.repmat(param, 1, Ncell)

            # Calculate histogram
            hist, edges = np.histogram(param, bins=bin_num) # single spin
            hist = hist * Ncell # with 3d box
            hist = hist / sum(hist) # normalize
            edges = edges[0:len(hist)] # shift bin edges to get the same length as data
            return hist, edges

        def spin_density(self,x,y,g):
            """
            Calculates distribution of spins in resonator
            """
            hist, edges = self.distribution(x,y,g)

            return hist, edges

        def larmor_density(self,x,y,theta_larmor):
            """
            Calculates distribution of Larmor frequency
            """
            hist, edges = self.distribution(x,y,theta_larmor)
            return hist, edges

        def purcell_density(self,x,y,gamma):
            """
            Calculates distribution of purcell rate in resomator
            """
            hist, edges = self.distribution(x,y,gamma)
            return hist, edges

        def ncell(self,x,y,param):
            """
            Number of cells in resonator
            """
            # Reshape g so we can append multiple values for each box section
            param=param.reshape(len(param),1)

            # Calculate the size of the boxes
            bucket = x.count(x[0]) # number of samples for each point in space
            x_box = abs(float(x[bucket-1]) - float(x[bucket]))
            y_box = abs(float(y[0]) - float(y[1]))
            z_box = x_box
            volume = x_box * y_box * z_box

            # Calculate number of spins in each cell
            no_spins_in_box = 1e7
            Ncell = round(no_spins_in_box * volume)
            return Ncell

        def purcell_rate(self,g,Q,*args,**kwargs):
            """
            Calculates the Purcell rate
            """
            k = self.omega / Q
            omega_s = kwargs.get('omega_s',self.omega)
            delta = self.omega - omega_s

            purcell = k * ((g**2) / (k**2) / (4 + delta**2))
            # purcell = (4*(g**2)) / k
            return purcell

        def purcell_factor(self,lambda_c,n,Q):
            """
            Calculates the Purcell enhancement induced by the cavity
            """
            F = ( 3 / (4*np.pi**2) ) * (lambda_c / n)**3 * ( Q / (self.w * self.t * self.l))
            return F

        def coupling(self,dbx,dby,*args,**kwargs):
            """
            Calculates coupling constant g, <m|Sx|m> * ue * sqrt(dby^2 + cos(theta) dbx^2)
            """
            theta = kwargs.get('theta',0) # Angle the static magnetic field is applied on
            ang = np.cos(theta)
            ue = sp.physical_constants["Bohr magneton"][0]
            g = [*map(lambda x,y: 0.47 * ue * np.sqrt(y**2 + x**2),dbx,dby)]
            g = np.asarray([x / sp.h for x in g])
            return g 

        def average_photon_number(self):
            """
            Calculates average photon number
            """
            n = (4 * k1 * Pin) / (sp.hbar * self.omega * (k1 + k2 + kL)**2)
            return n

        def cooperativity(self):
            """
            Calculates cooperativity
            """
            return

        def finesse(self):
            """
            Calculates finesse
            """
            return

