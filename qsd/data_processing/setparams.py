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
        self.__w = None
        self.__t = None
        self.__l = None
        self.__pen = None
        self.__omega = None
        self.__Z = None
        self.__N = 2
        self.__w_mesa = None
        self.__h_mesa = None
        self.__gap_ind = None

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

        self.__w = float(pd["w"])
        self.__t = float(pd["t"])
        self.__l = float(pd["l"])
        self.__pen = float(pd["pen"])
        self.__omega = float(pd["omega"])
        self.__w_cap = float(pd["w_cap"])
        self.__l_cap = float(pd["l_cap"])
        self.__gap_cap = float(pd["gap_cap"])
        self.__w_mesa = float(pd["w_mesa"])
        self.__h_mesa = float(pd["h_mesa"])
        self.__gap_ind = float(pd["gap_ind"])
        
        params = {'w':self.__w,
            't':self.__t,
            'l':self.__l,
            'pen':self.__pen,
            'omega':self.__omega,
            'Z':self.__Z
        }
        return params

    def param_list(self,x,I,Jnorm,paramfile):
        """
        Generates a text file which holds the parameters requiured for the COMSOL simulation
        """
        n = [abs(i) for i in x]
        idx = n.index(min(n))

        I0 = I[idx]
        J0 = I0/(2*(self.__w+self.__t)*self.__pen)
        pen_perp = self.__pen**2 / (2*self.__t)
        C = (0.506*np.sqrt(self.__w/(2*pen_perp)))**0.75
        l1 = self.__pen*np.sqrt(2*self.__pen/pen_perp)
        l2 = 0.774*self.__pen**2/pen_perp + 0.5152*pen_perp
        J2overJ1 = (1.008/np.cosh(self.__t/self.__pen)*np.sqrt(self.__w/pen_perp/
            (4*pen_perp/self.__pen - 0.08301*self.__pen/pen_perp)))
        J1 = Jnorm[idx]
        w_sub = 4*self.__w
        h_sub = 25e-06

        f = open(paramfile,'w')
        f.write('w_ind ' + str(self.__w) + '[m] width_of_inductor\n'
           'h_ind ' + str(self.__t) + '[m] thickness_of_inductor\n'
           'l_ind ' + str(self.__l) + '[m] length_of_inductor\n'
           'pen ' + str(self.__pen) + '[m] penetration_depth\n'
           'I0 ' + str(I0) + '[A/m] current_at_x=0\n'
           'J0 ' + str(J0) + '[A/m^3] current_density_at_x=0\n'
           'N ' + str(self.__N) + '\n'
           'w_sub ' + str(w_sub) + '[m] substrate_width\n'
           'h_sub ' + str(h_sub) + '[m] substrate_height\n'
           'pen_perp ' + str(pen_perp) + '[m] perpendicular_pen_depth\n'
           'C ' + str(C) + ' capacitance\n'
           'l1 ' + str(l1) + '[m]\n'
           'l2 ' + str(l2) + '[m]\n'
           'J2overJ1 ' + str(J2overJ1) + '\n'
           'J1 ' + str(J1) + '[A/m]\n'
           'w_mesa ' + str(self.__w_mesa) + '[m]\n'
           'h_mesa ' + str(self.__h_mesa) + '[m]\n'
           'gap_ind ' + str(self.__gap_ind) + '[m]'
           )

        f.close()


