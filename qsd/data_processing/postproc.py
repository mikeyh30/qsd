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
        self.__w = w
        self.__t = t
        self.__l = l
        self.__pen = pen
        self.__omega = omega
        self.__Z = Z
        
        self.__g = None

        self.__volume_cell = None

    def spinmap(self,xin,yin,spin_depth):
        """
            Defines the layer at which spins are implanted. At the moment, only specified for bulk doping
        """
        xs = xin[(yin >= -spin_depth) & (yin <= 0.0)]
        ys = yin[(yin >= -spin_depth) & (yin <= 0.0)]
        return xs,ys

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
        self.__g = 0.47 * ue * np.sqrt(By**2 + (ang**2) * Bx**2)
        return self.__g/sp.h

    def cut_line_spin_density(self,g):
        """
        Calculates the spin density for cut line section
        """
        self.__volume_cell = g * self.__t * self.__l
        rho =  sp.m_e / self.__volume_cell
        return rho

    def distribution(self,x,y,param,*args,**kwargs):
        """
        Method to calculate histogram
        """
        bin_num = kwargs.get('bins',50)
        Ncell = self.ncell(x,y,param)
        param = np.matlib.repmat(param, 1, Ncell)
        
        # Calculate histogram
        hist, edges = np.histogram(param, bins=bin_num) # single spin
        hist = hist * Ncell # with 3d box
        hist = hist / sum(hist) # normalize
        edges = edges[0:len(hist)] # shift bin edges to get the same length as data
        return hist, edges

    def spin_density(self,x,y,g,*args,**kwargs):
        """
        Calculates distribution of spins in resonator
        """
        bin_num = kwargs.get('bins',50)
        hist, edges = self.distribution(x,y,g,bins=bin_num)

        return hist, edges

    def larmor_density(self,x,y,theta_larmor,*args,**kwargs):
        """ 
        Calculates distribution of Larmor frequency
        """
        bin_num = kwargs.get('bins',50)
        hist, edges = self.distribution(x,y,theta_larmor,bins=bin_num)
        return hist, edges

    def purcell_density(self,x,y,gamma,*args,**kwargs):
        """
        Calculates distribution of purcell rate in resomator
        """
        bin_num = kwargs.get('bins',50)
        hist, edges = self.distribution(x,y,gamma,bins=bin_num)
        return hist, edges

    def ncell(self,x,y,param):
        """
        Number of cells in resonator
        """
        # Reshape g so we can append multiple values for each box section
        param=param.reshape(len(param),1)

        # Calculate the size of the boxes
        if type(x) != list:
            x = list(x)
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
        k = self.__omega / Q
        omega_s = kwargs.get('omega_s',self.__omega)
        delta = self.__omega - omega_s
        
        purcell = k * ((g**2) / (k**2) / (4 + delta**2))
        # purcell = (4*(g**2)) / k
        return purcell

    def purcell_factor(self,lambda_c,n,Q):
        """
        Calculates the Purcell enhancement induced by the cavity
        """
        F = ( 3 / (4*np.pi**2) ) * (lambda_c / n)**3 * ( Q / (self.__w * self.__t * self.__l))
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
        n = (4 * k1 * Pin) / (sp.hbar * self.__omega * (k1 + k2 + kL)**2)
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
