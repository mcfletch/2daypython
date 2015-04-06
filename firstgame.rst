Our First Game
==============

We are going to create a simple guessing game.

* We will choose a random number between 1 and 100
* We will ask the user to guess that number
* If they succeed, we'll say "Yay"
* If they don't get it right, we'll tell them whether they are:

  * too high
  * too low

* and then let them try again.

Breaking Down the Problem
-------------------------

What are the steps we are going to take:

* Choose a random `integer` between 1 and 100
* Remember the integer we chose
* Ask the user for a guess
* Test if the number they guessed is the number we chose
* To do one thing if the number does match
    * stop the guessing
    * print a congratulations
* To do something else if the number does not match
    * tell user if they are high or low
    * allow user to continue guessing

Part of that operation is a `loop` of things we want to do many times,
asking the user, checking the number, deciding whether the user has guessed 
correctly.

Choosing a Random Number
-------------------------

* Someone wrote a module that provides functions related to `random` numbers
* The module is called `random <https://docs.python.org/2/library/random.html>`_
* There is a function in it called `randint`
* How do we use that function?
* First we need to get the `module`

.. doctest::

    >>> import random
    >>> random # doctest:+ELLIPSIS
    <module 'random' from ...>

So how do we use the function? Let's ask:
    
.. code-block::

    >>> help(random.randint)

So apparently we can just do this to get a random number:

.. code-block::

    >>> random.randint( 1, 100 )
    34

Exercise: Naming the Number
---------------------------

We are going to create a script that will become our game.
Import the random module, and store the result of `random.randint`
in a variable.

.. literalinclude:: exercises/guessinggame/01random.py
    :language: python

Getting the User's Guess
------------------------

How do we get the user's guess? There's actually a built-in
function we can use to ask the user to type in their guess.
It is called `raw_input` (`input` on Python 3.x) and is 
available without needing any imports:

.. code-block:: python

    >>> raw_input( "What is your guess? " )
    What is your guess? 

.. note::

    There is a problem, raw_input returns a `str` **not**
    a number.

We need to convert what the user types into an `int` so that 
we can compare it to the value we've chosen. We can do that 
by passing the result of `raw_input` to the `int` type:

.. code-block:: python

    >>> guess = raw_input('What is your guess? ')
    What is your guess? 32
    >>> guess = int(guess)
    >>> guess
    32

Exercise: Ask the User to Guess
-------------------------------

Modify your game to ask the user to guess a number.
Convert their guess to an integer.

.. literalinclude:: exercises/guessinggame/input.py
    :language: python

Test for Success
----------------

When we want to compare two numbers, we use `operators`
that return True/False for comparisons:

.. doctest::

    >>> 32 == 45
    False

When we want to use that comparison to make a decision, 
we use an `if` statement:

.. doctest::

    >>> if 32 == 45:
    ...     print "Oh no, math is broken"
    ... elif 32 > 45:
    ...     print "Worse than we thought"
    ... else:
    ...     print "Oh good, carry on"
    ... 
    Oh good, carry on

.. note::

    * `==` **not** `=`
    * note the indentation, it's important
    * the `...` characters are just from the interpeter, they're not part of Python
    * the `else` block is only run if *no* other block matches

Exercise: Test for Success
--------------------------

* Modify your game to check for success.
* If the user was too high, tell them so
* If they were too low, tell them so
    
.. literalinclude:: exercises/guessinggame/03ifstatement.py
    :language: python

Looping
-------

* We need to let the user keep guessing
* We can use a loop to do that

.. doctest::

    >>> while n > 0:
    ...     print n
    ...     n = n-1
    ... 
    3
    2
    1

If we want something to keep going forever, we can use 
`True` as the test in the `while` statement
    
.. code-block:: python

    >>> import random
    >>> while True:
    ...     if random.randint(1,100) == 32:
    ...             print 'yay'
    ...             break
    ...     else:
    ...             print '.'
    ... 

Exercise: Let the User Try Again
---------------------------------

.. literalinclude:: exercises/guessinggame/04whileloop.py
    :language: python

Exercise: Just Give them 10 Guesses
-------------------------

.. literalinclude:: exercises/guessinggame/forloop.py
    :language: python

Make the Number Random
----------------------

.. literalinclude:: exercises/guessinggame/randomness.py
    :language: python
