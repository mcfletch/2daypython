More Math
=========

There are lots of ways we can combine numbers or modify them.

.. doctest::

    >>> count = 5.0
    >>> count * 3
    15.0
    >>> count / 3
    1.6666666666666667
    >>> count ** 2 # exponentiation
    25.0
    >>> count ** .5
    2.23606797749979
    >>> count % 3 # remainder
    2.0
    >>> count // 3 # quotient
    1.0
    >>> count * 3 + 2
    17.0
    >>> count * (3 + 2) # parenthesis group
    25.0
    >>> count / count
    1.0
    >>> count ** count
    3125.0

Exercise
--------

* Play with numbers, see if you can find an expression that crashes the interpreter
    
Advanced Exercise
------------------

* There are more operators we haven't seen here.
* See if you can figure out what these operators do.
* Hint: they work on the *internal* representation of numbers within the computer.

.. doctest::

    >>> 2 >> 1
    1
    >>> 2 << 1
    4
    >>> 2 << 2
    8
    >>> 1 & 2
    0
    >>> 1 & 3
    1
    >>> 1 ^ 2
    3
    >>> ~1
    -2
    >>> 1|2
    3
