Type Conversions
================

We can convert between various `types` of objects, often just 
by calling the `type` with the thing we want to convert:

.. doctest::

    >>> string = '32'
    >>> string
    '32'
    >>> int(string)
    32
    >>> float(string)
    32.0
    >>> str( int( string ))
    '32'
    >>> str( float( string ))
    '32.0'

.. doctest::
    
    >>> string = '32.6'
    >>> int(string)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '32.6'
    >>> float( string )
    32.6
    >>> int( float (string ))
    32
    >>> int( round( float( string ), 0 ))
    33
    >>> round( 32.6, 0 )
    33.0
    >>> round( 32.6, 1 )
    32.6

Exercise
~~~~~~~~

In the interpreter, multiply the strings '10' and '20' to get the integer result 200:
    
.. code-block:: python
    
    >>> first = '10'
    >>> second = '20'
    ...
    >>> print first * second # should print 200
