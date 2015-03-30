Math
====

Numbers are the most `fundamental` thing in a computer, everything 
else (text, graphics, sound) gets translated into numbers so that the 
computer can deal with them:

* to make an image brighter we add a value to each `pixel`
* to make audio lounder we add a value to each `sample`
* to make text ALL CAPS we convert each character (number) 
  to the equivalent uppercase character (number)
  
So we need to understand what we can do with numbers.

.. doctest::

    >>> 5.0
    5.0
    >>> 5 + 3
    8
    >>> 5 * 3
    15
    >>> 5 / 2
    2
    >>> 5 / 2.0
    2.5
    >>> 5 // 2.0
    2.0
    >>> 5 % 2.0
    1.0
    >>> 5 / 3.0
    1.6666666666666667

Anything surprising happening in there?

.. note::

    Making text ALL CAPS is actually a pretty involved thing to do.
    We used to do it by just subtracting 32 from the character-code, 
    but that doesn't work well for non-English languages.
    
    The complexity is normally handled by some already-written code
    that knows how to do the work in any language.
