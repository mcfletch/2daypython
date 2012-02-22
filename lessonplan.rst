Lesson Plan
===========

Basics
-----------

* variables, assignment, print

.. literalinclude:: exercises/basicvariables.py
    :language: python

* arithmetic

.. literalinclude:: exercises/basicarithmetic.py
    :language: python

* basic types

.. literalinclude:: exercises/basictypes.py
    :language: python

* type conversions

.. literalinclude:: exercises/basicconversions.py
    :language: python
    
    
* lists

.. literalinclude:: exercises/basiclists.py
    :language: python

Exercise
~~~~~~~~

* create, modify and display some variables

.. literalinclude:: exercises/basicexercise.py
    :language: python


List Indexing
-------------
    
* indexing

  .. image:: images/listindices.png
     :alt: Image showing indices aligned with spaces before each item in list

  * ``alist[i]`` looks up the index in the above scheme and gets the next item
  * ``alist[-i]`` looks up the index in the second line and gets the next item 


* list slicing 

  * ``alist[i:j]`` looks up the index ``i``, then includes all items until it reaches the index ``j``
  * you can leave off the index for start/end
  
    * ``alist[:j]`` retrieves all items from start (index 0) until we reach ``j``, this is, conveniently, the first ``j`` items
    * ``alist[i:]`` starts at index ``i`` and retrieves all items until we reach the end, this "skips" the first ``i`` items

.. literalinclude:: exercises/basicslicing.py
    :language: python

Exercise
~~~~~~~~

* slice and dice a list 

.. literalinclude:: exercises/basicsliceexercise.py
    :language: python


Logic and Loops
---------------

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

* scripts (since from here out we'll be giving them starter scripts)

  * Linux/Unix

    * ``#! /usr/bin/env python`` line
    * executable bit ``chmod 0755 <script>``
    
  * Windows 
  
    * filename/extension on Windows
    * PATHEXT on Windows

Exercise
~~~~~~~~

* filter values in a list to only include values whose square root is greater than 2

.. literalinclude:: exercises/iterexercise.py
    :language: python

Strings and Dictionaries
------------------------

* strings

  * strip 
  
    .. literalinclude:: exercises/stringstrip.py
        :language: python
  
  * split, join
  
    .. literalinclude:: exercises/stringsplit.py
        :language: python

* dictionaries

  * keys (must be immutable)
  * values (anything)
  * iterable, but un-ordered

    .. literalinclude:: exercises/dictdefinitions.py
        :language: python

Exercise
~~~~~~~~

* loop over list of strings, split into key: value pairs and add to dictionary

.. literalinclude:: exercises/dictexercise.py
    :language: python

Reading a File
--------------

* look at ``../sample_data.csv``, note how it looks like the data in the
  previous exercise
  
.. literalinclude:: sample_data.csv 

* this is a standard comma separated value data-file, possibly from some survey
  which asked test subjects various questions and subjected them to various 
  tests to assess their capabilities

.. literalinclude:: exercises/fileread.py
    :language: python

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
* docstrings

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

* more complex functions, return multiple values
* functions calling other functions

    .. literalinclude:: exercises/functionisolation.py
        :language: python

* explain how functions are part of good practices for readable, reusable code

Exercise
~~~~~~~~

* loop over list of list of floats calculating min, max, mean, total, median for each

Lesson Six
------------

* put all code into functions
* __name__ == '__main__'
* modules and importing

Exercise
~~~~~~~~

* something where students use a function we've provided in another file

Lesson Seven
------------

* opening a file
* reading a file
* command line arguments, sys.argv?

Exercise
~~~~~~~~
* read a nicely formatted, perfect data file into dictionary of lists

Lesson Eight
------------

* looping over a dictionary
* writing to a file
* string formatting

Exercise
~~~~~~~~
* using data from previous exercise calculate min, max, mean, median of each column. write stats to human-readable file.

Exercise
~~~~~~~~
* combine previous two exercises but now input file is imperfect (e.g. CSV with missing values)

Code Reuse
-----------

* using existing libraries can both save work and errors

  * for instance, the following will handle ``,`` characters encoded in your CSV files

    .. literalinclude:: exercises/reusecsv.py
        :language: python

  * existing libraries will also generally have functions you don't want to have to code yourself

    .. literalinclude:: exercises/reusenumpy.py
        :language: python
