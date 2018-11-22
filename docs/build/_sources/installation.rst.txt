Installation
============

This package has been designed for easy interfacing with Linux or Mac OS operating systems. It is possible to use this package on Windows operating systems, but the ssh commands may not work so well. I will modify the package for Windows at a later date.

This package has several dependencies. First, you must install numpy adnd scipy. The easiest way to do this is to use pip. If you do not have pip installed onn your compiter, it can be downloaded from the internet. Then, in a terminal winndow, type::

    pip install matplotlib
    pip install numpy
    pip install scipy


To install QSDCalcs, open type the command::

    pip install -i https://test.pypi.org/simple/ qsd

This will download the package to your computer. Next, you will need to download the COMSOL .mph file. This file is hosted at https://github.com/garethsion/qsd/blob/master/qsd/tests/cpw_vacuum_calcs.mph . Download this to your working directory.
