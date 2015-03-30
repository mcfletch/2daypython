Loops
=====

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
