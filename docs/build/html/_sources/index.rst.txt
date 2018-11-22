Quantum Spin Dynamics Resonator Calculations Documentation
==========================================================

Often when using coplanar waveguide resonators for quantum spin dynamics, it is desirable to understand certain critical figures of merit. However, the workflow required for determining these data is often quite laborious. This package details an automated procedure calling ssh protocols into remote machines..

Please note, this package is still as yet a work in progress. I will update a working 'ToDo' list frequently, and I will ocasionally be tidying up the code and folder sturcture.

Guide
^^^^^

.. toctree::
   :maxdepth: 2

   overview
   installation
   usage
   howitworks
   todo
   gallery
   resources
   license
   help

Package Library Classes
^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 3

   electromagnetics
   ssh_control
   data_processing

Examples
^^^^^^^^
The following examples show how to use the package in order to generate a cpw geometry, run the calculations on remote machines, and process the data for various figures of merit.

.. toctree::
   :maxdepth: 2

   current_density
   addremote
   remote_connection
   single_spin_coupling
   purcell_enhancement
   pulse_fidelity
   cutline_single_spin
   cutline_purcell

Indices and tables
^^^^^^^^^^^^^^^^^^

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
