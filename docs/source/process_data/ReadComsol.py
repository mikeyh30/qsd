#!/usr/bin/env python
"""
ReadComsol
"""

import numpy as np
import csv
from subprocess import call

class ReadComsol:
    """
    Ya
    """

    def __init__(self,file):
        """
        Ya
        """
        self.file = file

    def get_comsol_data(self):
        """
        Ya
        """
        rc = call("./get_comsol_data")

    def read_1D_comsol_data(self):
        """
        Ya
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
        Ya
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
        Ya
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
