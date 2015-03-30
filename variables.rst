Variables
=========

Variables are `names` that point to values (`objects`).
We used `count` before, but now we're going to count two things.
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

Exercise
--------

* Create a number of `variables` and compare them in your interpreter.
* What type of names work as `variables`? Can you include spaces or punctuation?

.. note::

    * What is the difference between `=` and `==`?
    * Should we have named our `variables` dog_count and cat_count?
    * Sometimes programmers are lazy and leave things out
    
