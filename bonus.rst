Bonus Material
==============

Larger Programs
---------------

* as programs become larger, we need to organise the program such that we can 
  manage the complexity of our projects
* we will tend to use common pieces of code in many places (we've seen how to 
  import such code already), so we collect that code and reuse it
* we want to group similar pieces of code into similar places so that it is 
  easy to find where a piece of code is later
  
* in Python, the basic unit of grouping is the "module", which is a single Python
  file that can be imported directly into another "module"
* in Python, sets of modules can be put into a "package" (a directory with a 
  special ``__init__.py`` file, we can then ``import package.module`` or, 
  more commonly ``from package import module``

* we normally want to formalize our program's interface to match posix standard,
  so we want to return 0 on success and 1 on failure.

Code Reuse
-----------

* using existing libraries can both save work and errors

  * for instance, the following will handle ``,`` characters encoded in your CSV files

    .. literalinclude:: exercises/reusecsv.py
        :language: python

  * existing libraries will also generally have functions you don't want to have to code yourself

    .. literalinclude:: exercises/reusenumpy.py
        :language: python

