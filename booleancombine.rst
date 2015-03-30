Boolean Combinations
====================
    
Logical combinations allow you to string together boolean tests
  
  * ``and``, ``or``, ``not``
  
.. doctest::

    >>> x = 23
    >>> y = 42
    >>> (x == y) or (x * 2 > y )
    True
    >>> (x == y) or (x > y)
    False
    >>> (x < y) and (y > 30)
    True
    >>> (x == y) or (not x > y)
    True  
