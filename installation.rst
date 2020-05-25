Installing Python at Home
==========================

These instructions are intended to get you an environment very similar to the one you’ll 
be using during the Coder’s Club. Before you start:

* you will be installing software from the internet, you **MUST** get permission 
  from the owner of the computer to do this (likely your parents)
* there are different instructions for Windows, Mac (Apple/OS-X) and Linux, you 
  need to choose the set for your computer

You do not need a particularly powerful computer to program. While most programmers use ridiculously 
powerful machines, you can start with any old machine.

What We are Doing
-----------------

At the end of this process, you should have:

* the programming language Python (version 2.7 on everything save Mac)
* the multimedia/graphics/audio library Pygame
* an editor for (Python) code (PyScripter, PyCharm, or MS Code)

.. note::

    You **did** get permission from the owner of the machine, right?
    Do that **now**.

Windows Installation 10+
---------------------------------------

We are going to download these packages to your computer and then run the installers we have downloaded:

* Follow the instructions at https://docs.python.org/3/using/windows.html and use the custom
  installation, choosing to install Python on the PATH for the machine.

Start a PowerShell window and test if you can run Python from the window::

  $ python 

.. note::

  If you can't run python this way, you likely have to add Python's directory to the PATH
  in system settings

Install pygame:

  $ python -m pip install pygame


Mac/OS-X Installation
---------------------

.. note:: 

    Appologies up-front, this is the least pleasant environment to setup.
    OS-X has Python installed, but most Python packages, and particularly Pygame,
    don't work well with the built-in Python interpreter.

You should follow `these instructions <http://programarcadegames.com/index.php?chapter=foreword&lang=en#section_0_1_2>`_
which will set you up with a **Python 3** environment, but are at least known to work.

* `PyCharm Community Edition <https://www.jetbrains.com/pycharm/download/>`_ can be used to edit code

Linux Installation 
--------------------

You need the following packages on Debian/Ubuntu machines (this includes the Raspberry Pi):

* python3 (this is likely already installed on a modern Linux)
* python3-pygame (you can install this either via apt/yum or using `pip3 install pygame`

You can install both packages on Ubuntu with:

.. code-block:: bash

    $ sudo apt-get install python3 python3-pygame

* https://code.visualstudio.com/ 

