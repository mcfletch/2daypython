Guessing Game
==============

We are going to create a simple guessing game.

* We will choose a random number between 1 and 100
* We will ask the user to guess that number
* If their guess is too high/low, we tell them that and let them try again
* When they succeed, we say "Yay"

Breaking Down the Problem (Pseudocode)
--------------------------------------

What are the steps we are going to take:

.. code-block:: python

    number = create_a_random_integer(1,100)
    until_the_user_succeeds:
        ask_for_number()
        give_user_guidance_if_high_or_low()
    print( 'congratulations' )

There are some things we don't know how to do (yet) in there:

* create_a_random_integer
* ask_for_number
* until_the_user_succeeds
* give_user_guidance_if_high_or_low

Create a Random Number
-------------------------

* Random numbers are a **huge** area of active research in computer science
* We don't actually care about that in our game, we just want something the user can't **easily** guess
* Someone wrote a module that provides functions related to (psuedo)-`random` numbers
* The module is called `random <https://docs.python.org/2/library/random.html>`_ and 
  it is documented in the Python documentation
* There is a function in it called `randint`

.. doctest::

    >>> import random
    >>> random # doctest:+ELLIPSIS
    <module 'random' from ...>
    >>> number = random.randint( 1, 100 )

* what does all that mean::

    random.randint # gets a name *inside* the "random" module
    ( ) # sends a *message* to that thing
    1, 100 # passes two parameters as part of that message
    number = # assigns the result of sending the message to a variable

* we are going to define our own functions in our next game: :doc:`trivia`

Exercise: Setup the Game Script
+++++++++++++++++++++++++++++++

We are going to create a script that will become our game.

* In `Idle` or `PyScripter` create a new file
* Save the empty file into your home directory (`H:\`)
* In the file:

  * `import` the module `random`
  * create a random integer and store it in a variable
  * print the variable (so we can see if it worked)

* Save the file
* Start `PowerShell`

  * <Win-R> then type `Powershell` <enter>
  
* In Powershell, navigate to your home directory
* Try to run your script 

.. code-block:: powershell

    c:\> h:
    h:\> dir 
    game.py
    h:\> python game.py
    34
    h:\> 

Review: Setting up the Game Script
+++++++++++++++++++++++++++++++++++
    
.. literalinclude:: exercises/guessinggame/01random.py
    :language: python

Ask for a Number
----------------

* How do we ask the user for `input`?
* There's a function that does it for us (notice a pattern?)
* It is called `raw_input <https://docs.python.org/2/library/functions.html#raw_input>`_ and
  it is a `built-in` (which means it is always available in Python 2)
* It takes an argument that is the `prompt` you want to present to the user and returns 
  **the text** (string) they typed

.. code-block:: python

    >>> guess = raw_input( "What is your guess? " )
    What is your guess? 23
    >>> guess
    23
    >>> type(guess)
    <type 'str'>

.. note::

    If you are using Python 3 `raw_input` has been renamed to `input`.

We need to break down our pseudo-code for this step:

.. code-block:: python

    guess = raw_input()
    guess = convert_to_int(guess)

We can convert a string-containing-an-int into an integer with the following:

.. doctest::

    >>> guess = '32'
    >>> guess = int(guess)
    >>> type(guess)
    <type 'int'>
    >>> guess
    32

Exercise: Ask for a Number
++++++++++++++++++++++++++

* Modify your game to give the user one chance to guess the number
* Remember to convert their input to an integer
* print the guess *and* the number (again, to let us see if it is working)

Review: Ask for a Number
+++++++++++++++++++++++++

.. literalinclude:: exercises/guessinggame/02input.py
    :language: python

Until the User Succeeds
-----------------------

We need to understand what we mean by until the user succeeds:

* We want to do a set of (many) actions many times

  * ask_for_number
  * give_user_guidance_if_high_or_low
  
* We want to test to see if they have succeeded (a comparison)

  * if they have *not* succeeded, we want to keep looping 
  * if they *have* succeeded, we want to stop looping

When we see a set of operations we want to do many times, we are 
looking at a `loop`. This particular example looks like a `while`
loop because we want to keep doing it `while` something is True:

.. code-block:: python

    number = create_a_random_integer(1,100)
    while not success:
        ask_for_number()
        give_user_guidance_if_high_or_low()
    print( 'congratulations' )

* If the <test> succeeds

  * All of the statements that are within the `while` block are executed
  * Those statements may change the values referenced in the <test>
  * When the block of statements finishes, the test is re-run to determine whether to run the block again

.. topic:: Indentation

    Most programming languages do **not** use indentation to declare blocks.
    In most common languages, there are braces {} or words which declare the start and end of blocks.
    However, almost every major programming language also includes a style-guide that 
    tells people how they should format their blocks-of-code in order to make the code easy to read.

.. doctest::

    >>> n = 3
    >>> while n > 0:
    ...     print n
    ...     n = n-1
    ... 
    3
    2
    1
        
So what is "success" in our game?

* The user's guess is `==` to the random number

So our test would look like:

.. code-block:: python

    while not (guess == number):
        do_something()

.. note::

    We could also spell it as `guess != number` rather than `not (guess == number)`
    
* What's wrong with that?
* What happens on the first trip through the loop, where you haven't yet asked the user for a guess?
* The interpreter is going to run the **test** before it runs `do_something()`
* We need to set guess to a value that can't possibly be right so that we will get into the while loop:

.. code-block:: python

    guess = 0
    while not (guess == number):
        do_something()

Exercise: Loop Until Success
++++++++++++++++++++++++++++

* Modify your script so that the user is asked to guess until they succeed

.. note::

    Pretty hard, eh? You can stop before you guess the number by hitting <ctrl-c>
    on the keyboard to `interrupt` the script.

Review: Loop Until Success
++++++++++++++++++++++++++

.. literalinclude:: exercises/guessinggame/03whileloop.py
    :language: python

Give Guidance
-------------

* We want to do something `if` one of these two cases is True:

  * Guess is too high
  * Guess is too low
  
* This sounds like an `if` statement

.. code-block:: python
    
    if <test>:
        do_first_thing()
    elif <othertest>:
        do_other_thing()

* How do we spell `too high` and `too low`?

.. doctest::

    >>> 32 < 45
    True
    >>> 45 > 32
    True 

Exercise: Give Guidance
+++++++++++++++++++++++

* Modify your game to tell the user when they are too high or too low

Review: Give Guidance
+++++++++++++++++++++

.. literalinclude:: exercises/guessinggame/04ifstatement.py
    :language: python

Exercise: Congratulate the User
-------------------------------

.. literalinclude:: exercises/guessinggame/05congratulations.py
    :language: python

Extra Exercises
---------------

* Modify your script to track the number of guesses and report to the user
* Figure out the best strategy to win the game (hint: investigate `binary search`)
