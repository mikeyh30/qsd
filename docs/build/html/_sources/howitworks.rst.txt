How the COMSOL Simulation Works
===============================

In order to model the vacuum field fluctuations in a superconducting microwave resonator, we model the structure as a two-dimenisional wire. This is a simple magnetic fields AC/DC simulation, and we are interested in solving Ampere's Law for the cpw structure.

The first step in the procedure is to calculate the spatial dependence of the vacuum current fluctuations. There are several different ways to do this, all of which are untilately equivalent. In this package at the moment I use two different methods, as i am testing which one is the easiest to deal with in simulation.

One method of finding the current density is given in the paper "Reaching the quantum limit of sensitivity in electron spin resonance" (Bienfait, et al, 2015):

.. math::

    \delta J(x) = 
    \begin{cases}
    \delta J(0) \left[1-(2x/w)^{2}  \right]^{-1/2},     for \left|x\right| \le \left|\frac{1}{2} w - \lambda^{2} / (2b) \right| \\
    \delta Jt(\frac{1}{2} w) exp \left[(\frac{1}{2}w - \left|x\right|) b/ \lambda^{2} \right] , for \left|\frac{1}{2} w - \lambda^{2} / (2b) \right| \le \left|x\right| \le \frac{1}{2} w\\
    (1.165/\lambda) (wb)^{1/2} \delta J(0) , for x=\frac{1}{2} w 
    \end{cases}


