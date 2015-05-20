List Indexing
=============

How do we get objects *out* of :doc:`lists` after we've put them in?

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
    
We call this `indexing` into the list, and we call the numbers inside 
the square brackets `indices` or an `index`.

* how do indexing numbers work?

  .. image:: images/listindices.png
     :alt: Image showing indices aligned with spaces before each item in list

  * ``alist[i]`` looks up the index in the above scheme and gets the next item
  * ``alist[-i]`` looks up the index in the second line and gets the next item 

List Slicing
------------

Sometimes you don't want to get just 1 value from a list, you want to get a list
that is just *part* of another list:  

  * ``alist[i:j]`` looks up the index ``i``, then includes all items until it reaches the index ``j``
    * you can leave off the index for start/end
  
  * ``alist[:j]`` retrieves all items from start (index 0) until we reach ``j``, this is, conveniently, the first ``j`` items
  * ``alist[i:]`` starts at index ``i`` and retrieves all items until we reach the end, this "skips" the first ``i`` items

.. doctest::

    >>> counts = [1, 2, 3, 4, 5]
    >>> counts
    [1, 2, 3, 4, 5]
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

.. note::

    Bonus Material

    You can also specify a "step" in your slices:
    
    .. doctest::
    
        >>> counts[::2] # every other item, starting at 0
        [1, 3, 5]
        >>> counts[1::2] # every other item, starting at 1
        [2, 4]
        >>> counts[::-1] # the whole list, stepping backward
        [5, 4, 3, 2, 1]
        >>> counts[-1:1:-1] # start at index -1, step backward while index is > 1
        [5, 4, 3]

* the convenience function :py:func:`range` creates lists with ranges of integers

.. doctest::

    >>> range( 5 )
    [0, 1, 2, 3, 4]
    >>> range( 2, 5 )
    [2, 3, 4]
    >>> range( 5, 2, -1 )
    [5, 4, 3]

Other Objects
--------------

You can slice and index other objects:

.. doctest::

    >>> string = "a big string"
    >>> string[0]
    'a'
    >>> string[:5]
    'a big'
    >>> string[-6:]
    'string'
    >>> tup = (0,1,2,3,4)
    >>> tup[2]
    2
    >>> tup[:2]
    (0, 1)
    >>> tup[-2:]
    (3, 4)

    
Exercise
---------

* slice and dice a list 

.. literalinclude:: exercises/basicsliceexercise.py
    :language: python
