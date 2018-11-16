#!/usr/bin/env python
"""
This program sets the parameters required for simulation. 
"""

import numpy as np
import os
from subprocess import call

class SetParams:
    def __init__(self):
        self.w = None
        self.t = None
        self.l = None
        self.pen = None
        self.omega = None
        self.Z = None
        self.N = 2

    def set_params(self):
        self.w = 10e-06
        self.t = 50e-09
        self.l = 8.194e-03
        self.pen = 200e-09
        self.omega = 7.3e09
        self.Z = 50

        params = {'w':self.w,
            't':self.t,
            'l':self.l,
            'pen':self.pen,
            'omega':self.omega,
            'Z':self.Z
        }
        return params

    def param_list(self,x,I,Jnorm,file):
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

        paramFile = str(os.getcwd() + file)

        f = open(paramFile,'w')
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


