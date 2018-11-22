To Do List
==========

This code is still a work in progress. There are quite a few things I still have to do. A detailed list is given below:

* Include EPR spectra code to calculate the eigenvalues of the EPR transitions. This then forms a key value going into the calculation for the single spin coupling, i.e. we need to calculate :math:`\left< m_{f} \right| \hat{S}_{x} \left| m_{f} \right>` for the single spin coupling.

.. math::
  

    g=\left< m_{f} \right| \hat{S}_{x} \left| m_{f} \right>\gamma_{e}\sqrt{\delta B^{2}_{y} + \left(\cos \theta \right) \delta B^{2}_{x} }

* Automate CST procedure to calculate impedance and external q factor

* Specify the distribution of spins for the single_spin_coupling example

* Weight the purcell_enhancement and pi pulse fidelity examples by contribution to the signal

* Apply a fidelity measure to the pi pulse
