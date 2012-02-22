Lesson Plan
===========

You may want to follow along with some of these examples, you can start an 
interactive Python prompt (an "interpreter") such as you see here by running
``python`` (the basic Python interpreter) or ``ipython`` (a more friendly 
interpreter).

Basics
------

(Matt)

* variables, assignment, print

.. doctest::

    >>> count = 5.0
    >>> print 'count', count
    count 5.0
    >>> count = count + 3.0
    >>> print 'new count',count
    new count 8.0

* variables point to values (objects), *not* to other variables

.. doctest::

    >>> first = 1
    >>> second = 2
    >>> second = first
    >>> second
    1
    >>> first = 3
    >>> first
    3
    >>> second
    1
    
* arithmetic

.. doctest::

    >>> count = 5.0
    >>> count + 3
    8.0
    >>> count * 3
    15.0
    >>> count / 3
    1.6666666666666667
    >>> count ** 2 # exponentiation
    25.0
    >>> count ** .5
    2.23606797749979
    >>> count % 3 # remainder
    2.0
    >>> count // 3 # quotient
    1.0
    >>> count * 3 + 2
    17.0
    >>> count * (3 + 2)
    25.0

* basic types

.. doctest::

    >>> count = 36
    >>> print count
    36
    >>> count / 10 # surprising?
    3
    >>> irrational = 3.141592653589793
    >>> irrational
    3.141592653589793
    >>> label = "irrational, 'eh"
    >>> label2 = 'count "this"'
    >>> label3 = '''python has these too'''
    >>> label4 = """but they are just a different way to write the same thing"""
    >>> print label, label2, label3, label4
    irrational, 'eh count "this" python has these too but they are just a different way to write the same thing
    >>> print label + label2
    irrational, 'ehcount "this"
    >>> None # doesn't show up
    >>> print None
    None
    >>> print True
    True
    >>> print False
    False
    >>> True == 1
    True
    >>> False == 1
    False
    >>> False == 0
    True

* type conversions

.. doctest::

    >>> string = '32'
    >>> string
    '32'
    >>> int(string)
    32
    >>> float(string)
    32.0
    >>> str( int( string ))
    '32'
    >>> str( float( string ))
    '32.0'

.. doctest::
    
    >>> string = '32.6'
    >>> int(string)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '32.6'
    >>> float( string )
    32.6
    >>> int( float (string ))
    32
    >>> int( round( float( string ), 0 ))
    33
    >>> round( 32.6, 0 )
    33.0
    >>> round( 32.6, 1 )
    32.6
    
* lists

.. doctest::

    >>> integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> integers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> integers.append( 11 )
    >>> integers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    >>> integers.insert( 0, -1 )
    >>> integers
    [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    >>> len(integers)
    12
    >>> integers.append( 'apple' )
    >>> integers
    [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 'apple']

   
Exercise
~~~~~~~~

* exercise scripts (in the ``exercises`` folder)

  * Linux/Unix

    * ``#! /usr/bin/env python`` line
    * executable bit ``chmod 0755 <script>``
    
    .. code-block:
    
        $ cd exercises 
        $ ./basicexercise.py
    
  * Windows 
  
    * filename/extension on Windows
    * PATHEXT on Windows
    * cygwin setup

* edit the file ``exercises/basicexercise.py``

  * create, modify and display some variables
  
* run the file with ``python basicexercise.py`` from the ``exercises`` directory
  or ``./basicexercise.py`` if you prefer.

.. literalinclude:: exercises/basicexercise.py
    :language: python


List Indexing
-------------

(Matt)
    
* indexing

  .. image:: images/listindices.png
     :alt: Image showing indices aligned with spaces before each item in list

  * ``alist[i]`` looks up the index in the above scheme and gets the next item
  * ``alist[-i]`` looks up the index in the second line and gets the next item 

.. doctest::

    >>> counts = [0,1,2,3,4]
    >>> counts[0]
    0
    >>> counts[1]
    1
    >>> counts[2]
    2
    >>> counts[-1]
    4
    >>> counts[-2]
    3
    >>> counts[-4]
    1
    >>> counts[-5]
    0
    >>> counts[-6]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    >>> 

* list slicing 

  * ``alist[i:j]`` looks up the index ``i``, then includes all items until it reaches the index ``j``
  * you can leave off the index for start/end
  
    * ``alist[:j]`` retrieves all items from start (index 0) until we reach ``j``, this is, conveniently, the first ``j`` items
    * ``alist[i:]`` starts at index ``i`` and retrieves all items until we reach the end, this "skips" the first ``i`` items

.. doctest::

    >>> counts = [1, 2, 3, 4, 5]
    >>> counts
    [1, 2, 3, 4, 5]
    >>> counts = [1, 2, 3, 4, 5]
    >>> counts[1:]
    [2, 3, 4, 5]
    >>> counts[:-1]
    [1, 2, 3, 4]
    >>> counts[1:-1]
    [2, 3, 4]
    >>> counts[99:]
    []
    >>> counts[:-99]
    []
    >>> counts[3:8]
    [4, 5]

Exercise
~~~~~~~~

* slice and dice a list 

.. literalinclude:: exercises/basicsliceexercise.py
    :language: python


Logic and Loops
---------------

(Mike)

* loops using for x in y
* indenting, "suites" of commands, *python* is not normal here (braces)

.. literalinclude:: exercises/iterforxiny.py
    :language: python

* if, elif, else

  * only do the suite if the "check" matches
  * else is for when no other check matches (and is optional)
  
* comparisons, boolean operators

  * ``==`` (are they equal) vs ``=`` (assign value)
  * ``>=``, ``<=``, ``!=`` (not equal)
  * ``and``, ``or``, ``not``

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

(Matt)

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

.. doctest::

    >>> count = 53
    >>> mean = 37.036
    >>> label = 'DMX Score'
    >>> '{},{},{}'.format( label, count, mean )
    'DMX Score,53,37.036'
    >>> '{!r} for {} items {:0.2f}'.format( label, count, mean )
    "'DMX Score' for 53 items 37.04"  

Dictionaries
------------

(Mike)

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

* loop over list of strings, split into key: value pairs and add to dictionary

.. literalinclude:: exercises/dictexercise.py
    :language: python

Reading a File
--------------

(Mike)

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
  piped into your program at the ``bash`` prompt

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

(Matt)

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

(Matt)

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

(Matt)

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

(Mike)

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

(Mike)

* while using ``print`` is fine when you are directly communicating with a user,
  you will often want to output data in a structured format for future processing
* when writing data to be read by computers
* files can be opened in "write" mode by passing ``'w'`` as the ``mode`` parameter
* the standard module ``sys`` has two file handles already opened for output

  * stdout -- where most client programs expect your primary output 
  * stderr -- where most client programs expect error messages, warnings etc.

.. literalinclude:: exercises/outputbasic.py
    :language: python

Exercise
~~~~~~~~

* modify your ``moduleexercise.py`` script to write the summary information for 
  each column processed into a CSV file where each row is the original column 
  label (the first row in the file) and the mean value for that row

Errors and Reading Tracebacks
-----------------------------

(Mike)

* does your script fail if you point it at ``../bad_sample_data.csv``?
* what does the traceback tell you?

Exercise
~~~~~~~~

* modify your ``moduleexercise.py`` so that it can parse ``../bad_sample_data.csv``
  as well as any file in the ``../real_data/`` directory.
  
  * assume that missing values should be set equal to 0.0
  * assume that comments (lines starting with '#') and blank lines should be 
    ignored

Exercise
~~~~~~~~

* modify your script to load *multiple* files passed from the command line
* verify that *all* of the data records are represented in the final values

