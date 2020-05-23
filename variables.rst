Variables
==========

* We created a `variable`, but what are `variables`?
* They are `names` that point to values
* We can change the value to which they point

.. doctest::

    >>> dogs = 2
    >>> cats = 1
    >>> dogs
    2
    >>> cats
    1
    >>> dogs > cats 
    True
    >>> dogs = 1
    >>> dogs > cats
    False
    >>> dogs = 3
    >>> dogs
    3
    >>> dogs > cats
    True
    >>> cats + dogs
    4

Exercise
--------

* Create a number of `variables` and compare them in your interpreter.
* What type of names work as `variables`? Can you include spaces or punctuation?
* What is the difference between `=` and `==`?
* Should we have named our `variables` dog_count and cat_count?
    
Extra Exercise
-------------------

* What should the following print? (Try to answer without running it)

.. code-block:: python

    >>> a,b = 1,2
    >>> b,a = a,b
    >>> c,b = a,b
    >>> b,b = b,c
    >>> print b
    
