String Comparisons
==================

We can also compare text (known as `strings`):

.. doctest::

    >>> "a" > "b"
    False
    >>> "a" < "b"
    True
    >>> "a" < "A"
    False
    >>> "z" < "Z"
    False
    >>> "this" > "th" # having "something more" means you are > ('i' is compared to '')
    True
    >>> "this" > "tho" # the first difference determines the result ('i' is compared to 'o')
    False

.. note::

    Why is "a" > "A"?
    
    Your computer represents the two characters with different numbers internally.
    Those numbers happen to be arranged such that "a" (97) is greater than "A" (65).

