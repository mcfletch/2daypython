Type Conversions
================

We can convert between various `types` of objects, often just 
by calling the `type` with the thing we want to convert:

.. doctest::

    >>> value = '32'
    >>> value
    '32'
    >>> int(value)
    32
    >>> float(value)
    32.0
    >>> str( int( value )) # note `str` not `string`
    '32'
    >>> str( float( value ))
    '32.0'

.. doctest::
    
    >>> value = '32.6'
    >>> int(value)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '32.6'
    >>> float( value )
    32.6
    >>> int( float (value ))
    32
    >>> int( round( float( value ), 0 ))
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
