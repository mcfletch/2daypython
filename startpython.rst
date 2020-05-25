Starting Python
===============

.. note::

  If you are working on your computer at home, you may need to
  :doc:`install Python<installation>` on your machine first.
  You will likely need the help of the owner of the machine 
  (e.g. your parents) to accomplish that.

.. note::

  If you don't yet know how to use the console/shell on your machine,
  you should read :doc:`shellsandconsoles` first and then 
  return here.

Students at Home
-----------------

On Linux or Mac machines open a console/terminal and type::

  $ python3
  Python 3.7.5 (default, Apr 19 2020, 20:18:17) 
  [GCC 9.2.1 20191008] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

You can get out of the interpreter by hitting <CTRL-D> or <COMMAND-D> 
(that is, hold down the Ctrl key and tap the D key).

You may wish to install a capable editor, such as 
Microsoft's Visual Studio Code to edit your Python code.

Windows Users 
-------------

Open a PowerShell console and type::

  $ python3

You can exit the interpreter by hitting <CTRL-Z> <ENTER> at the start 
of a line (that is, hold down the Ctrl key and tap the D key, release Ctrl and 
tap the enter key).

TDSB Students 
--------------

.. note::

  These instructions were written in 2016, they are likely out of date
  and it *should* be far easier to start a console in Python today.

* Get logged into your TDSB account

  * The same account you use for school https://aw.tdsb.on.ca

* Start Python

  * |startbutton| Start Button | type "py" | Choose "Idle" or "Pyscripter 3.7"

  * If you don't see Python, choose another machine but *log out* first
  * If you are offered a choice between Python 2 and Python 3, choose Python 3

If you've started `Idle` or `Pyscripter` you are running an 
`Integrated Development Environment` which includes a Python Interpreter window.
Normally this shows up at the bottom or bottom-right corner of the IDE.
You'll recognize it because it has a `prompt` that has 3 `greater than` symbols::

    >>> 


The Interpreter
---------------

If you've just started `Python` you will see a (black) window with the prompt:

.. code-block:: bash 

  $ python
  Python 3.7.5 (default, Apr 19 2020, 20:18:17) 
  [GCC 9.2.1 20191008] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

Don't worry if the numbers are slightly different, or there are different descriptions
of the program. What we care about is that you are seeing the `>>>` prompt and that the 
version of Python starts with 3.  If your version starts with 2, such as 2.6 or 2.7,
then you'll need to deal with some minor changes throughout the course.

.. note::

  You can exit the interpreter by hitting your platform's ``<end of input>`` 
  key combination.  On Windows this is ``<ctrl-z><enter>``. On Linux ``<ctrl-d>``,
  on Mac ``<command-d>``

So you've started Python, you should be looking at the interpreter. The interpreter
is just a program that listens to what you type, tries to turn it into Python
code, and prints the results back to you.  It likely
looks something like this::

  >>>

.. note::
    In the interpreter, the ``>>>`` prompt tells you that you can enter Python 
    code and have it executed when you hit ``<Enter>``.

.. note::

    If you are using the IPython interpreter, the prompt may look like::

      In [1]:
    
    instead of `>>>`


.. |startbutton| image:: images/windowsstart.png
                 :alt: Windows Start Button
