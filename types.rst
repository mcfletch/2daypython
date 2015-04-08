Types
=====

We've seen a number of different `types` of values so far, let's review them:

Integers (:py:class:`int`)
--------------------------

.. doctest::

    >>> 23
    23
    >>> 45
    45
    >>> 69
    69

Floats (:py:class:`float`)
--------------------------

    >>> 23.0
    23.0
    >>> 45.0
    45.0
    >>> -39.
    -39.0
    >>> 1e100 # a googol
    1e+100

Strings (:py:class:`str`)
-------------------------

    >>> "this"
    'this'
    >>> 'that'
    'that'

Booleans (:py:class:`bool`)
---------------------------
    >>> True 
    True 
    >>> False
    False

Exercise
--------

.. doctest::

    >>> type(0)
    <type 'int'>

* Explore the types for other data-types we've seen.

.. note::

    What do those `()` characters mean in `type(0)`?
    
    We are asking a "thing" called `type` to "act" upon a single thing,
    which is our integer value `0`.
    The thing `type` has a piece of code (a "function" or "method")
    that tells it what to do when it is "asked to act" ("called") 
    on a set of things ("arguments" or "parameters").
    Here the set of arguments we are passing is a single value, but later on we will 
    see how to pass multiple arguments into functions which support multiple arguments.
    
    We'll see how to write our own functions later in this tutorial.
    A "method" is a function which is "attached" to an object, we'll use these 
    throughout the tutorial, but this tutorial does not yet cover how to write 
    our own objects.

Extra Exercise
-------------------

* Play with type and the results of type

.. doctest::

    >>> type(4)(3.14159)
    3
    >>> type("this")(3.14159)
    '3.14159'
    >>> type(type)
    <type 'type'>
    >>> type(type)(type)
    <type 'type'>
