Booleans
========
    
Reduces down to the statement: "if this is True, do that, otherwise do that".
Computers, being binary (on/off) machines work very easily with on/off choices such as 
boolean logic.

* almost any object can be tested for "boolean truth"
    
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
