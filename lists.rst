Lists
=====

* lists are "collections of things" which have a particular order
* you can add and remove items to the list (unlike `tuples`)
* lists can contain any type of object, including other lists

.. doctest::

    >>> integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> integers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> integers.append( 11 )
    >>> integers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    >>> integers.insert( 0, 12 )
    >>> integers
    [12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    >>> len(integers)
    12
    >>> sorted(integers)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
    >>> integers # why didn't integers change?
    [12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    >>> integers.sort()
    >>> integers # the .sort() method did an "in place" sort
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
    >>> integers.append( 'apple' )
    >>> integers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 'apple']

.. doctest::

    >>> lists = [ [1,2],[3,4],[5,6]]
    >>> lists
    [[1, 2], [3, 4], [5, 6]]
    >>> lists[0]
    [1, 2]
    
.. note::

    What did `integers.append( 11 )` mean?
   
    Here the object `integers` had a piece of code attached to it (we call these "methods")
    which was written to "add an object to the end of THIS list".
    By writing `integers.append` we "looked up" this piece of code in the `integers` list.
    When we added the `( 11 )` to the statement we asked that piece of code (`append`) to act 
    on a single integer object `11` within the *context* of the `list` object.

.. note::

    Python's interactive interpreter has a `help` function that allows you to get documentation
    on a particular `type` of object, such as `list`.  The help text normally includes all of the 
    "methods" that are available, a description of the parameters for each method, and normally 
    a "docstring" (human description) for the method explaining what it does, and occasionally 
    how it does it.

    .. code-block:: python
        
        >>> help( list ) # type <q> to exit the help

Tuples
------

Tuples are pretty-much like lists, except that you can't *change* them after you create them:

.. doctest::

    >>> integers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> integers
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> len(integers)
    10
    >>> integers.append 
    Traceback (most recent call last):
      File "/usr/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest default[3]>", line 1, in <module>
        integers.append
    AttributeError: 'tuple' object has no attribute 'append'

We *normally* don't use tuples like this, we normally use tuples as a way to 
pack together things in a "lightweight structure" or "object", so in :doc:`heartclick`
we used a tuple to store a direction:

.. doctest::

    >>> direction = (1,1)
    >>> x,y = direction 
    >>> direction = (x+1,y-2)
    >>> direction
    (2, -1)


:doc:`listindexing` shows you how to work with the items inside a list.
