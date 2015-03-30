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

    print "Hello, World!"

and save that to your home directory as `helloworld.py`.

Getting to the Command Prompt
--------------------------------

We'll use the `PowerShell` environment from `Microsoft` as our `command line`.

* Click the |startbutton| and type `PowerShell`
* You should see a prompt showing your `home directory`
* If you list the directory you should see your Python script

.. code-block:: bash

    > dir

and we can try to run it with:

.. code-block:: bash

    > python helloworld.py
    Hello, World!


.. |startbutton| image:: images/windowsstart.png
                 :alt: Windows Start Button
