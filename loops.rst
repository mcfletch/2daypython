Loops
=====

Let's review the `while` loop:

* `while` a `test` is True, keep doing a `suite` of things

.. doctest::

    >>> x = 4
    >>> while x > 0:
    ...     print(x)
    ...     x = x - 1
    ... 
    4
    3
    2
    1

We can imagine iterating over a `list` using the following:
    
.. doctest::

    >>> counts = [1, 2, 3, 4, 5]
    >>> i = 0
    >>> while i < len(counts):
    ...     count = counts[i]
    ...     print(count)
    ...     i = i + 1
    ... 
    1
    2
    3
    4
    5

But honestly, that's a bit of a pain, because we are going to do this a **lot**, so we 
have a way of spelling that in a cleaner format:
    
.. doctest::

    >>> counts = [1, 2, 3, 4, 5]
    >>> for count in counts:
    ...     print(count)
    ... 
    1
    2
    3
    4
    5

.. topic:: Suites of Commands

    Python is one of only a small number of languages that uses indentation to control
    what is "inside" a loop or if-statement.  Most languages use `{}` braces or 
    pairs of words, such as `do` and `done`.

.. code-block:: bash

    for var in a,b,c,d
    do 
        echo "Variable is ${var}"
        ls ${var}
    done 

.. literalinclude:: exercises/iterforxiny.py
    :language: python

* loops can "nest" further loops (or other structures)

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
