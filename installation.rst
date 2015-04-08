Installing Python at Home
==========================

These instructions are intended to get you an environment very similar to the one you’ll be using during the Coder’s Club. Before you start:

* you will be installing software from the internet, you MUST get permission from the owner of the computer to do this (likely your parents)
* there are different instructions for Windows, Mac (Apple/OS-X) and Linux, you need to choose the set for your computer

You do not need a particularly powerful computer to program. While most programmers use ridiculously powerful machines, you can start with any old machine.

What We are Doing
-----------------

At the end of this process, you should have:

* the programming language Python (version 2.7 on everything save Mac)
* the multimedia/graphics/audio library Pygame (version 1.9)
* an editor for (Python) code (PyScripter, Eric or <mac editor>)

.. note::

    You **did** get permission from the owner of the machine, right?
    Do that **now**.

Windows Installation (XP, Vista, 7, 8+)
---------------------------------------

We are going to download these packages to your computer and then run the installers we have downloaded:

* `32-bit Python 2.7.9 <https://www.google.com/url?q=https%3A%2F%2Fwww.python.org%2Fftp%2Fpython%2F2.7.9%2Fpython-2.7.9.msi&sa=D&sntz=1&usg=AFQjCNEyD6jodxsQkkJUnb_JKfu_iC74Jw>`_
* `32-bit Pygame 1.9.1 <http://www.google.com/url?q=http%3A%2F%2Fpygame.org%2Fftp%2Fpygame-1.9.1.win32-py2.7.msi&sa=D&sntz=1&usg=AFQjCNGjJTZQp3_d-_42T882jSr7Pdyrcw>`_
* `Pyscripter IDE <https://pyscripter.googlecode.com/files/PyScripter-v2.5.3-Setup.exe>`_

You will need to click through installation warnings for each of those.

Mac/OS-X Installation
---------------------

Appologies up-front, this is the least pleasant environment to setup.
OS-X has Python installed, but most Python packages don't work well with the built-in 
Python interpreter.
You should follow `these instructions <http://programarcadegames.com/index.php?chapter=foreword&lang=en#section_0_1_2>`_
which will set you up with a **Python 3** environment, but are at least known to work.

Linux Installation 
--------------------

You need the following packages on Debian/Ubuntu machines (this includes the Raspberry Pi):

* python2.7 (this is likely already installed)
* python-pygame
* eric  (a full-featured Python IDE, for non-Raspberry Pi devices, if you are using Rasbian you can use Idle)

You can install them at the command-prompt with:

.. code-block:: bash

    $ sudo apt-get install python2.7 python-pygame eric
