Variables
=========

Variables are `names` that point to values (`objects`).
Remember how a big part of programming is giving names to things?
Let's count some dogs and cats:

.. doctest::

    >>> dogs = 2
    >>> cats = 1
    >>> dogs
    2
    >>> cats
    1
    >>> dogs > cats 
    True
    >>> dogs = cats
    >>> dogs > cats
    False
    >>> dogs = 3
    >>> dogs
    3
    >>> dogs > cats
    True
    >>> cats + dogs
    4

Try it now.

.. note::

    * What is the difference between `=` and `==`?
    
