Boolean Tests
==============

When we want to make a decision in a program, we formulate the decision 
in the form::

  if (something is true):
    do this thing
    and this other thing
  else: 
    otherwise do this thing 
    and some other thing

the `something is true` test checks the :doc:`boolean truthiness <booleans>`
of the expression. So an empty list, the number 0, an empty string, or any
thing which is `falsey` will skip the `if` block and instead run the `else`
block.

We can include :doc:`math expressions <basicmath>`:, 
:doc:`boolean combinations <booleancombine>`, 
the results of functions, or any other expression in the test.

`if` Statements 
---------------

  * only do a given "suite" of statements if the "check" matches
  * else is for when no other check matches (and is optional)
  * elif is short-form for `else if` which you will see in other 
    languages such a javascript

.. note::

  Suites of Statements
  .....................

  In Python, we use indentation (the number of spaces at the start of the
  line) to indicate the structure of the program. Other languages will use
  `{}` characters, or even words such as `if` and `fi` to indicate the 
  start and end of a suite of things that are done together.

.. doctest::

    >>> x = 32
    >>> if x < 5:
    ...     print('hello')
    ... elif (x+4 > 33):
    ...     print('hello world')
    ... else:
    ...     print('world')
    ... 
    hello world

.. note::

    Technical Tidbit
    
    Your computer is formed of tiny electrical switches where a current in one 
    "wire" can prevent or allow a current from flowing in another "wire".
    Below all the levels of abstraction, when the computer decides "if this is True" 
    it is checking whether a value can flow through the second "wire".

.. note::

    Recall that comparisons are boolean operators

      * ``==`` (are they equal) vs ``=`` (assign value)
      * ``>=``, ``<=``, ``!=`` (not equal)

* logical combinations allow you to string together boolean tests
  
  * ``and``, ``or``, ``not``
  
.. doctest::

    >>> x = 23
    >>> y = 42
    >>> (x == y) or (x * 2 > y )
    True
    >>> (x == y) or (x > y)
    False
    >>> (x < y) and (y > 30)
    True
    >>> (x == y) or (not x > y)
    True  
