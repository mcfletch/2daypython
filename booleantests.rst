Boolean Tests
=============
    
* if, elif, else

  * only do a given "suite" of commands if the "check" matches
  * else is for when no other check matches (and is optional)

.. doctest::

    >>> x = 32
    >>> if x < 5:
    ...     print('hello')
    ... elif (x+4 > 33):
    ...     print('hello world')
    ... else:
    ...     print('world')
    ... 
    hello world

.. note::

    Technical Tidbit
    
    Your computer is formed of tiny electrical switches where a current in one 
    "wire" can prevent or allow a current from flowing in another "wire".
    Below all the levels of abstraction, when the computer decides "if this is True" 
    it is checking whether a value can flow through the second "wire".

.. note::

    Recall that comparisons are boolean operators

      * ``==`` (are they equal) vs ``=`` (assign value)
      * ``>=``, ``<=``, ``!=`` (not equal)

* logical combinations allow you to string together boolean tests
  
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
