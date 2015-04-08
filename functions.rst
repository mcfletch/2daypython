Simple Functions
=================

* previous exercise introduced code reuse
* simple functions, one returned value

.. literalinclude:: exercises/functionsimple.py
    :language: python
        
* variable scope

Exercise
--------

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
--------

* in ``readdata.py`` group the code that makes a dictionary from
  the data into a function that returns the dictionary
* also put the code that makes lists into a function that returns
  several lists
* have both of these functions take a file name as an argument and
  call the file reading function you've already written
* call these functions and use the data they return to make
  the rest of the code work 

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
--------

* modify your ``moduleexercise.py`` script take the file to process from the 
  (bash) command line
