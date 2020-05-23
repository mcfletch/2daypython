Starting Python
===============

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

You can install Python 3 from http://www.python.org . Remember to say 
"yes" when it asks if you want to make Python available on your path.

Then open a PowerShell console and type::

  $ python3

You can exit the interpreter by hitting <CTRL-Z> <ENTER> at the start 
of a line
(that is, hold down the Ctrl key and tap the D key, release Ctrl and 
tap the enter key).

TDSB Students 
--------------

* Get logged into your TDSB account

  * The same account you use for school

* Start Python

  * |startbutton| Start Button | type "py" | Choose "Idle" or "Pyscripter 3.7"

  * If you don't see Python, choose another machine but *log out* first

If you've started `Idle` or `Pyscripter` you are running an 
`Integrated Development Environment` which includes a Python Interpreter window.
Normally this shows up at the bottom or bottom-right corner of the IDE.
You'll recognize it because it has a `prompt` that has 3 `greater than` symbols::

    >>> 


The Interpreter
---------------

If you've just started `Python` you will just see a black window with the prompt:

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
  key combination.  On Windows this is ``<ctrl-z><enter>``.

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
