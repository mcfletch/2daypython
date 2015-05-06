Exceptions and Tracebacks
-------------------------

* so far we've ignored situations where errors occurred, but real software needs 
  to handle errors or unexpected conditions all the time

.. doctest::

    >>> value = ' Aquamarine Falcon '
    >>> float( value )
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: could not convert string to float:  Aquamarine Falcon 

* when functions call other functions, the system creates a "stack" of "frames",
  an uncaught error will, by default, print out a "traceback" of these frames

  * when something goes wrong, you use the traceback to help you find out where
    and what the problem was
  * in *python* the traceback is ordered from "top" to "bottom", that is, the 
    "frame" printed first in the traceback ("<stdin>" in the example below) is 
    the "top level" caller
  * each frame is a function which was running (not yet complete) when the 
    uncaught error was encountered
  * in *python*, the last line of the traceback is a string representation of 
    the ``Exception`` which was raised, which generally attempts to be a useful 
    description of what went wrong
  
.. doctest::
      
    >>> from functionarguments import *
    >>> rows = split_rows( open('../sample_data.csv').read().splitlines()[1:] )
    >>> first,second = extract_columns( rows, 1, -2 )
    >>> first,second = extract_columns( rows, 30 )
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "functionarguments.py", line 15, in extract_columns
        result.append( extract_column( rows, column ))
      File "functionarguments.py", line 8, in extract_column
        result.append( row[column] )
    IndexError: list index out of range

* it is possible to catch these ``Exceptions`` in Python by using 
  a special type of block around the code in which the exception may occur

.. doctest::

    >>> value = '  Aquamarine Falcon '
    >>> try:
    ...     value = float( value )
    ... except ValueError as err:
    ...     value = value.strip()
    ... 
    >>> value
    'Aquamarine Falcon'

.. note::

    We can catch multiple Exception types using ``except (ValueError,TypeError) as err``
    instead.
    
.. note::

    The syntax for catching exceptions changes between Python 2.x and 3.x, in Python 
    3.x the syntax becomes ``except ValueError, TypeError as err``
  
Exercise
~~~~~~~~

* does your script fail if you point it at ``../bad_sample_data.csv``?

  * if not, congratulations; you pass
  * if so, what does the traceback tell you?

* (if necessary) modify your ``moduleexercise.py`` so that it can parse 
  ``../bad_sample_data.csv`` as well as any file in the ``../real_data/`` 
  directory
  
  * catch the case where the first column is a quoted, comma-separated name,
    convert the name to ``first last`` rather than ``last, first``
  * assume that missing (numeric) values should be set equal to 0.0
  * assume that comments (lines starting with '#') and blank lines should be 
    ignored
