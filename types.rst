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
    >>> 2**20
    1048576
    >>> -2**20
    -1048576
    >>> 10**100 # a googol as an integer
    10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

Integers are "whole numbers" just as you learned in school. The can be positive or
negative and (in python) can be arbitrarily large, though your computer might 
run out of memory trying to think about some of them.

We can enter integers in different formats too:

.. doctest::

    >>> 0x10
    16
    >>> 0x20
    32
    >>> 0x21
    33
    >>> 0x9
    9
    >>> 0xa
    10
    >>> 0xb
    11
    >>> 0o10
    8
    >>> 0o20
    16
    >>> 0o77
    63
    >>> 0o70
    56


Floats (:py:class:`float`)
--------------------------

.. doctest::

    >>> 23.0
    23.0
    >>> 45.0
    45.0
    >>> -39.
    -39.0
    >>> 1e100 # a googol in scientific notation
    1e+100

Floating point numbers are a way of representing numbers-with-fractions in a computer.
Behind the scenes they are actually an approximation of the binary fraction closest to
the number you are trying to represent. So a fraction that is exactly 1/2, 1/4, 1/8,
1/16, 1/32, etc will be precisely represented, but any other fraction will be an 
approximation of the value.

.. doctest::

    >>> .5
    0.5
    >>> .25
    0.25
    >>> 1/3
    0.3333333333333333
    >>> f'%0.30f'%(1/3)
    '0.333333333333333314829616256247'


Strings (:py:class:`str`)
-------------------------

    >>> "this"
    'this'
    >>> 'that'
    'that'

Strings, internally, are a sequence of `code points` which represent the 
characters in the text. There are a large number of different ways that
computers encode and decode text (called `encodings`). So when a program
wants to read or write text to a file or the network, the string will
be turned from the `internal` representation (called `unicode`) to the 
external representation (called `binary` or `bytes`).

We can add characters to strings that are otherwise hard type type by
using an `escape code` which is a back-slash character `\\` followed by
a special character (for common codes) or the numeric code-point of the
character.

.. doctest::

    >>> '\u27a2'
    '➢'
    >>> '\n'
    '\n'
    >>> print('\ta\tb') # doctest: +NORMALIZE_WHITESPACE
            a       b


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
    <class 'int'>

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
    <class 'type'>
    >>> type(type)(type)
    <class 'type'>
