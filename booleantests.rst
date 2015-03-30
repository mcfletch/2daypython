Boolean Tests
=============
    
* if, elif, else

  * only do a given "suite" of commands if the "check" matches
  * else is for when no other check matches (and is optional)

.. doctest::

    >>> x = 32
    >>> if x < 5:
    ...     print 'hello'
    ... elif (x+4 > 33):
    ...     print 'hello world'
    ... else:
    ...     print 'world'
    ... 
    hello world

.. note::

    Technical Tidbit
    
    Your computer is formed of tiny electrical switches where a current in one 
    "wire" can prevent or allow a current from flowing in another "wire".
    Below all the levels of abstraction, when the computer decides "if this is True" 
    it is checking whether a value can flow through the second "wire".

.. note::

    Recall that comparisons are boolean operators

      * ``==`` (are they equal) vs ``=`` (assign value)
      * ``>=``, ``<=``, ``!=`` (not equal)

* logical combinations allow you to string together boolean tests
  
  * ``and``, ``or``, ``not``
  
.. doctest::

    >>> x = 23
    >>> y = 42
    >>> (x == y) or (x * 2 > y )
    True
    >>> (x == y) or (x > y)
    False
    >>> (x < y) and (y > 30)
    True
    >>> (x == y) or (not x > y)
    True  

Loops
-----

* `while` something is True, keep doing "this set of things"

.. doctest::

    >>> x = 10
    >>> while x > 0:
    ...     print x
    ...     x = x - 1
    ... 
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1

.. doctest::

    >>> counts = [1, 2, 3, 4, 5]
    >>> i = 0
    >>> while i < len(counts):
    ...     count = counts[i]
    ...     print count
    ...     i = i + 1
    ... 
    1
    2
    3
    4
    5

* loops using `for x in y` are syntactic "sugar" for that last while loop, this pattern is 
  referred to as "iterating over" an object, and is extremely common

.. doctest::

    >>> counts = [1, 2, 3, 4, 5]
    >>> for count in counts:
    ...     print count
    ... 
    1
    2
    3
    4
    5

* "suites" of commands, *python* is not normal here (most languages use `{}` braces or 
  pairs of words, such as `do` and `done`)

.. code-block:: bash

    for var in a,b,c,d
    do 
        echo "Variable is ${var}"
        ls ${var}
    done 

.. literalinclude:: exercises/iterforxiny.py
    :language: python

* the suites can "nest" with further for-loops (or other structures)

.. literalinclude:: exercises/iternest.py
    :language: python

.. note::

    The ``enumerate`` function we use in the above sample can be thought of as 
    doing this::
    
        result = []
        for i in range( len( rows )):
            result.append( (i,rows[i]))
        return result 
    
    but is actually implemented in a more efficient manner.

.. literalinclude:: exercises/iterfilter.py
    :language: python

Exercise
~~~~~~~~

* construct lists by iterating over other lists
* use conditions to only process certain items in a list 
* use conditions and a variable to track partial results

.. literalinclude:: exercises/iterexercise.py
    :language: python

String Manipulation
-------------------

* strip (remove whitespace or other characters)

.. doctest::

    >>> value = '  25.3  '
    >>> value
    '  25.3  '
    >>> value.strip()
    '25.3'
    >>> quoted = '"this"'                                                                                                                             
    >>> quoted                                                                                                                                        
    '"this"'
    >>> quoted.strip('"')
    'this'
  
* split, join

.. doctest::

    >>> row = 'Silver Deer,69,-0.115,0.993,-0.12,25,violet'
    >>> components = row.split( ',' )
    >>> components
    ['Silver Deer', '69', '-0.115', '0.993', '-0.12', '25', 'violet']
    >>> print "\n".join( components )
    Silver Deer
    69
    -0.115
    0.993
    -0.12
    25
    violet
    >>> not_all_strings = [ 'Silver Goat', 45, -.333, .75, .08, 5, 'violet' ]
    >>> "\n".join( not_all_strings )
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sequence item 1: expected string, int found

* `format <http://docs.python.org/library/string.html#formatstrings>`_

.. todo:: this is *extremely* distracting, there is obvious complexity and the students get side-tracked

.. doctest::

    >>> count = 53
    >>> mean = 37.036
    >>> label = 'DMX Score'
    >>> '{0},{1},{2}'.format( label, count, mean )
    'DMX Score,53,37.036'
    >>> '{0!r} for {1} items {2:0.2f}'.format( label, count, mean )
    "'DMX Score' for 53 items 37.04"  

Dictionaries
------------

* a.k.a. hash-tables in other languages, have special syntax in most scripting 
  languages

  * keys must be immutable (technically, hashable)
  * values (anything)

.. literalinclude:: exercises/dictdefinitions.py
    :language: python

* you can add, remove, reassign

.. doctest::

    >>> dictionary = {}
    >>> dictionary
    {}
    >>> dictionary['this'] = 'those'
    >>> dictionary
    {'this': 'those'}
    >>> dictionary['those'] = 23
    >>> dictionary
    {'this': 'those', 'those': 23}
    >>> len(dictionary)
    2
    >>> dictionary['this'] == 'those'
    True
    >>> del dictionary['those']
    >>> dictionary
    {'this': 'those'}
    >>> 'those' in dictionary
    False
    >>> 'this' in dictionary
    True
    >>> dictionary['those']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'those'

* only one entry for each equal-hash-and-compare-equal key

  * you can thus use a dictionary to confirm/create uniqueness
  * values *must* compare equal *and* have the same "hash", this is 
    "computer equal", not "human equal", though Python tries to make 
    "computer equal" a bit more human e.g. with floats/ints

.. doctest::
  
    >>> dictionary = {'this':'that'}
    >>> dictionary[ ' this ' ] = 'thar'
    >>> dictionary
    {'this': 'that', ' this ': 'thar'}
    >>> dictionary[ 45 ] = 8
    >>> dictionary[ 45.0 ] = 9
    >>> dictionary
    {'this': 'that', ' this ': 'thar', 45: 9}
    >>> # Super Bonus Ask During Coffee Question: why is the key 45 and not 45.0?
    
* iterable, but un-ordered, so don't depend on the order of items 

.. literalinclude:: exercises/dictiteration.py
    :language: python
  
Exercise
~~~~~~~~

* loop over a list of strings, split into key: value pairs and add to dictionary

.. literalinclude:: exercises/dictexercise.py
    :language: python

Reading a File
--------------

* look at ``../sample_data.csv``, note how it looks like the data in the
  previous exercise
  
.. literalinclude:: sample_data.csv 

* this is a standard comma separated value data-file, possibly from some survey
  which observed animals and subjected them to various (humane) tests which 
  generated measurements.  Let's poke around in it:

.. doctest::
  
    >>> reader = open( '../sample_data.csv', 'r') # r is for "read" mode
    >>> reader #doctest: +ELLIPSIS
    <open file '../sample_data.csv', mode 'r' at 0x...>
    >>> content = reader.read()
    >>> len(content) 
    995
    >>> reader.close()
    >>> lines = content.splitlines()
    >>> len(lines)
    21
    >>> lines[0]
    'Subject,Count,DMX Score,Coda Score,Vinny Score,Zim Score,Subject Choice'
    >>> lines[1]
    'Dodgerblue Lemming,30,-0.988,0.154,-6.41,36,yellow'
    >>> lemming = lines[1]
    >>> columns = lemming.split(',')
    >>> columns
    ['Dodgerblue Lemming', '30', '-0.988', '0.154', '-6.41', '36', 'yellow']
    >>> measurement = columns[2]
    >>> measurement
    '-0.988'
    >>> type(measurement)
    <type 'str'>
    >>> measurement = float( measurement )
    >>> measurement
    -0.988
    >>> type(measurement)
    <type 'float'>

* the previous loaded the whole file into memory at one go, we could also 
  have iterated over the file line-by-line.
  
.. doctest::

    >>> reader = open( '../sample_data.csv', 'r')
    >>> header = reader.readline()
    >>> header # note the '\n' character, you often need to do a .strip()!
    'Subject,Count,DMX Score,Coda Score,Vinny Score,Zim Score,Subject Choice\n'
    >>> for line in reader:
    ...     print float(line.split(',')[2])
    ... 
    -0.988
    0.035
    ...

* the special file ``sys.stdin`` can be used to process input which is being 
  piped into your program at the ``bash`` prompt (we'll see two more special 
  pipes in `Writing (Structured) Files`_ below.

.. literalinclude:: exercises/argumentsstdin.py
    :language: python

.. code-block:: bash 

    $ cat ../sample_data.csv | ./argumentsstdin.py 
    -0.988
    0.035
    -0.898
    0.913
    ...

.. note::

  file objects keep an internal "pointer" (offset, bookmark) which they
  advance as you iterate through the file.  Regular files on the 
  file-system can be "rewound" or positioned explicitly.  File-like 
  objects such as pipes often cannot provide this functionality.

    
Exercise
~~~~~~~~

* read data from ``../sample_data.csv`` so that you have a list of strings,
  one string for each line in the file
* use code from ``dictexercise.py`` to again map names to colours and
  print the colour of a "Firebrick Coyote"
* use code from ``iterexercise.py`` to turn data into columns and
  find out which animal was spotted most frequently

.. literalinclude:: exercises/filereadexercise.py
    :language: python

Simple Functions
----------------

* previous exercise introduced code reuse
* simple functions, one returned value

.. literalinclude:: exercises/functionsimple.py
    :language: python
        
* variable scope

Exercise
~~~~~~~~

* copy your code from ``filereadexercise.py`` into ``readdata.py`` and
  turn the code that reads data from a file into a function that returns
  a list of strings
* have the function take a file name as an argument

.. literalinclude:: exercises/readdata.py
    :language: python

Functions as Building Blocks
----------------------------

* grouping code in small, logical chunks helps you reuse it
* docstrings

.. literalinclude:: exercises/functionreuse.py
    :language: python

Exercise
~~~~~~~~

* in ``readdata.py`` group the code that makes a dictionary from
  the data into a function that returns the dictionary
* also put the code that makes lists into a function that returns
  several lists
* have both of these functions take a file name as an argument and
  call the file reading function you've already written
* call these functions and use the data they return to make
  the rest of the code work 

Modules
-------

* using code from other files, modules and importing
* put all code into functions
* __name__ == '__main__'

.. literalinclude:: exercises/moduledemo1.py
    :language: python

.. literalinclude:: exercises/moduledemo2.py
    :language: python

.. literalinclude:: exercises/pretty_print.py
    :language: python

Exercise
~~~~~~~~

* write a function that finds the mean of a list of numbers and use
  it to find the mean of each of the score columns in ``sample_data.csv``
* use your functions in ``readdata.py`` by importing them

  * you will need to modify ``readdata.py`` so that it doesn't print
    anything when you import it

.. literalinclude:: exercises/moduleexercise.py
    :language: python

Arguments and Return Codes
--------------------------

* as you will recall from the ``bash`` session, programs have return codes
  which invoking programs will check to see whether the program succeeded
* main function and the "entry point" for scripts

  * scripting languages execute their code line-by-line, so they don't have a 
    ``void main() {}`` entry point as in ``C``
  * putting the main actions inside a function doesn't seem that useful 
    until you discover that most Python packaging tools can generate wrapper 
    scripts that invoke a particular function (such as main, here)

.. literalinclude:: exercises/argumentsmain.py
    :language: python

* command line arguments, sys.argv

.. literalinclude:: exercises/argumentsargv.py
    :language: python

* most real-world applications *also* want optional parameters, for those 
  see the `OptParse (for Python 2.6 and below) <http://docs.python.org/library/optparse.html>`_ or 
  `ArgParse (for Python 2.7 and above) <http://docs.python.org/library/argparse.html>`_ modules

Exercise
~~~~~~~~

* modify your ``moduleexercise.py`` script take the file to process from the 
  (bash) command line

Writing (Structured) Files
--------------------------

* while using ``print`` is fine when you are directly communicating with a user,
  you will often want to output data in a structured format for future processing
* files can be opened in "write" mode by passing ``'w'`` as the ``mode`` parameter
* the standard module ``sys`` has two pipe handles already opened for output,
  these are similar to the pipe handle ``sys.stdin`` we saw in `Reading a File`_.

  * stdout -- where most client programs expect your primary output 
  * stderr -- where most client programs expect error messages, warnings etc.

.. literalinclude:: exercises/outputbasic.py
    :language: python

Exercise
~~~~~~~~

* modify your ``moduleexercise.py`` script to write the summary information for 
  each (numeric) column processed into a CSV file where each row is the original 
  column label (the first row in the file) and the mean value for that row

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
    ... except ValueError, err:
    ...     value = value.strip()
    ... 
    >>> value
    'Aquamarine Falcon'

.. note::

    We can catch multiple Exception types using ``except (ValueError,TypeError), err``
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

Bonus Exercise
~~~~~~~~~~~~~~
    
* modify your script to load *multiple* files passed from the command line
* check for duplicate subject names

Using Existing Libraries
------------------------

* Generally speaking, you should prefer to use pre-written modules to handle 
  common tasks.  The Python standard library and the thousands of Python 
  packages and extensions mean that you normally would *not* write this type of 
  low-level code yourself.

.. literalinclude:: exercises/reusecsv.py
    :language: python

Bonus Exercise
~~~~~~~~~~~~~~

* rewrite your code to use the python standard `csv <http://docs.python.org/library/csv.html>`_
  library to parse the CSV data
* use the built-in min, max and sum functions to calculate summary information 
  on your columns, rather than using your custom-written functions 

Numpy
-----

* `numpy <http://numpy.scipy.org>`_ is a powerful package for use in scientific compuation with Python
* you can readily rewrite many of our samples (and far more involved processes)
  just by combining the tools Numpy already provides
  
.. literalinclude:: exercises/reusenumpy.py
    :language: python

Bonus Exercise 
~~~~~~~~~~~~~~

* using ``numpy``, load the ``sample_data.csv`` data-set and play with the columns 
  of data to determine what relationship the columns have to one another

  
.. |startbutton| image:: images/windowsstart.png
                 :alt: Windows Start Button
