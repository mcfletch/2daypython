String Comparisons
==================

We can also compare text (known as `strings`):

.. doctest::

    >>> "a" > "b"
    False
    >>> 'a' == "a"
    True
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
    You can see the code-point for a character with the function `ord`.

.. doctest::

    >>> ord('a')
    97
    >>> ord('A')
    65

.. topic:: Do the Quotes Matter?

    In **Python** the type of quote characters you use doesn't matter, it's just 
    whatever is convenient for you. In other languages the single quote `'` is often 
    used for single-characters, while the double quote `"` is used for 
    multiple character strings.
