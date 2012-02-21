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

  * `alist[i]` looks up the index in the above scheme and gets the next item
  * `alist[-i]` looks up the index in the second line and gets the next item 


* list slicing 

  * `alist[i:j]` looks up the index `i`, then includes all items until it reaches the index `j`
  * you can leave off the index for start/end
  
    * `alist[:j]` retrieves all items from start (index 0) until we reach `j`, this is, conveniently, the first `j` items
    * `alist[i:]` starts at index `i` and retrieves all items until we reach the end, this "skips" the first `i` items

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

* comparison, if statements

.. literalinclude:: exercises/iterfilter.py
    :language: python

* scripts (since from here out we'll be giving them starter scripts)

  * Linux/Unix

    * `#! /usr/bin/env python` line
    * executable bit `chmod 0755 <script>`
    
  * Windows 
  
    * filename/extension on Windows
    * CMDEXT on Windows

Exercise
~~~~~~~~

* filter values in a list to only include values whose square root is greater than 2

.. literalinclude:: exercises/iterexercise.py
    :language: python

Lesson Three
------------

* strings, strip, split, join
* dictionaries

Exercise
----------

* loop over list of strings, split into key: value pairs and add to dictionary

Lesson Four
------------

* simple functions, one returned value
* explain arguments, scope, etc
* zip function?
* help and dir?

Exercise
----------

* loop over two lists of integers building new list of max values from either list. students write max_val function.

Lesson Five
------------

* more complex functions, return multiple values
* functions calling other functions
* explain how functions are part of good practices for readable, reusable code

Exercise
----------

* loop over list of list of floats calculating min, max, mean, total, median for each

Lesson Six
------------

* put all code into functions
* __name__ == '__main__'
* modules and importing

Exercise
----------

* something where students use a function we've provided in another file

Lesson Seven
------------

* opening a file
* reading a file
* command line arguments, sys.argv?

Exercise
----------
* read a nicely formatted, perfect data file into dictionary of lists

Lesson Eight
------------

* looping over a dictionary
* writing to a file
* string formatting

Exercise
----------
* using data from previous exercise calculate min, max, mean, median of each column. write stats to human-readable file.

Exercise
----------
* combine previous two exercises but now input file is imperfect (e.g. CSV with missing values)
