Variables
=========

Variables are `names` that point to values (objects):

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
    
Exercise
~~~~~~~~

* edit the file ``exercises/basicexercise.py``

  * create, modify and display some variables
  
* run the file with ``python basicexercise.py`` from the ``exercises`` directory
  or ``./basicexercise.py`` if you prefer.

.. literalinclude:: exercises/basicexercise.py
    :language: python
