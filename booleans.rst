Booleans
========

* A special type of number that represents Truth/Falseness
* Remember we want to be able to tell the computer `if this is true, do that`
* In **python** almost any object can be used as a boolean
    
.. doctest::

    >>> bool( 0 )
    False
    >>> bool( 1 )
    True
    >>> bool( [] )
    False
    >>> bool( ['this'] )
    True
    >>> bool( 0.0 )
    False
    >>> bool( 1.0 )
    True
    >>> bool( '' )
    False 
    >>> bool( 'this' )
    True
    >>> bool( None )
    False
