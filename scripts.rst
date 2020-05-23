Scripts/Programs
================

You might have guessed that programmers don't actually re-type everything
every time the computer loads. There must be a way for a programmer to 
save the instructions we've been typing into the `interpreter` and run 
them later.

While other languages have more involved setup, the steps for creating 
and running a Python `script` (a small program) are:

* save the commands as a `plain text` file to the hard-disk
* run the plain-text file using `python` from the `command line`

Creating a Script
-----------------

In `Idle` or `Pyscripter` create a new file with the content:

.. code-block:: python

    print("Hello, World!")

and save that to your home directory (H:\) as `helloworld.py`.

.. note::

    If you are using `Python 2`, the content should be:
    
    .. code-block:: python

        print "Hello, World!"
    

Getting to the Command Prompt
--------------------------------

We'll use the `PowerShell` environment from `Microsoft` as our `command line`.

* Press and hold the "Windows" key, and hit the "R" key

  * a dialog will appear from which you can run commands
  
* Type `powershell` <enter>
* You should see a command prompt
* Change directory to your `home directory`

.. code-block:: powershell

    PS c:\Users\mcfletch> h:
    PS h:\somewhere> cd \
    PS h:\>

* If you list the directory you should see your Python script

.. code-block:: bash

    PS h:\> dir

and we can try to run it with:

.. code-block:: bash

    PS h:\> python helloworld.py
    Hello, World!
