#!/usr/bin/env python
import numpy as np
import os
from subprocess import call

file = cpw_parameters.txt

x=[]
y=[]
with open(file, 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        x.append(row[0])
        y.append(row[1])
x = np.asarray((x),dtype=float)
y = np.asarray((y),dtype=float)
return x,y
