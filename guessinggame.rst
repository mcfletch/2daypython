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

    # create a random number
    # loop until success
        # get user's number as integer
        # compare with the number 
            # print out guidance

Code Walk Through
-----------------

Here's what the final script might look like:

.. literalinclude:: exercises/guessinggame/05congratulations.py
    :language: python

Create a Random Number
-------------------------

* Someone wrote a module that provides functions related to (psuedo)-`random` numbers
* The module is called :py:mod:`random`
* There is a function in it called :py:func:`random.randint`

.. code-block:: python

    # load the library of code (module) called random
    import random
    # random is a module full of functions
    # one of which is randint()
    # we want to *remember* our random integer for later...
    number = random.randint(1,100)

* what does all that mean::

    random.randint # gets a name *inside* the "random" module
    ( ) # sends a *message* to that thing
    1, 100 # passes two parameters as part of that message
    number = # assigns the result of sending the message to a variable

* we are going to define our own functions in our next game: :doc:`trivia`

Exercise: Setup the Game Script
+++++++++++++++++++++++++++++++

We are going to create a script that will become our game.

* In `Idle` or `PyScripter` create a new file (our **script**)

  * File | New Window

* Save the empty script into your home directory (H:\)

  * File | Save As

* In the script type:

  .. code-block:: python

      import random
      number = random.randint(1,100)
      print(number)

* Save the script again
* Run the script with Idle <F5> or PyScripter <F9>

Ask for a Number
----------------

* How do we ask the user for `input`?
* Recall that the function for this is called :py:func:`raw_input`
* It takes an argument that is the `prompt` you want to present to the user and returns 
  **the text** (string) they typed

.. code-block:: python

    guess = raw_input('What is your guess? ')
    # ick, guess is a str, we want an int
    guess = int(guess)

.. note::

    If you are using Python 3.x you need to use :py:func:`py3:input` instead of :py:func:`raw_input`.

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

What is success in this game? Success is when the user's guess is equal to the number.

.. code-block:: python

    success = (guess == number)

We want to **keep** asking until the user succeeds:

.. code-block:: python

    while not success:
        ...
        success = (guess==number)

.. doctest::

    >>> n = 3
    >>> while n > 0:
    ...     print n
    ...     n = n-1
    ... 
    3
    2
    1
        

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

Give Guidance and Congratulations
---------------------------------

* We want to do something `if` one of these two cases is True:

  * Guess is too high (> number)
  * Guess is too low (< number)
  
* This sounds like an `if` statement

.. code-block:: python
    
    if <test>:
        do_first_thing()
    elif <othertest>:
        do_other_thing()
    else:
        do_thing_when_other_tests_false()

Exercise: Give Guidance
+++++++++++++++++++++++

* Modify your game to tell the user when they are too high or too low

Review: Give Guidance
+++++++++++++++++++++

.. literalinclude:: exercises/guessinggame/05congratulations.py
    :language: python

Extra Exercises
---------------

* Modify your script to track the number of guesses and report to the user
* Figure out the best strategy to win the game
