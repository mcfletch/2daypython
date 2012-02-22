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
  which observed animals and subjected them to various (humane) tests which 
  generated measurements

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

* grouping code in small, logical chunks helps you reuse it

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

Structured Output
-----------------

* while using ``print`` is fine when you are directly communicating with a user,
  you will often want to output data in a structured format for future processing

  
Exercise
~~~~~~~~

* modify your ``moduleexercise.py`` script take the file to process from the 
  (bash) command line

Errors and Reading Tracebacks
-----------------------------

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
