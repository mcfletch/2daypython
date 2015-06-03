Trivia Game
===========

.. topic:: Last Week!

    * This is our last week for Coding Club!
    * You should keep playing at home. See :doc:`installation`
    * This project will *not* be completed today!
    * Learning to code requires you to *try* and *keep trying* until 
      you understand
    * There are lots of other ways to learn to code. See :doc:`links`

Our Trivia Game works like so:

* We load some trivia questions
* We ask the user each question in turn
* Each level has an increasing point reward
* If the user gets a question wrong, their points are halved
* If the user gets 3 questions wrong, they lose everything
* If the user decides to quit (enter no answer), they exit with their current score

What it Looks Like
------------------

This is what running the game should look like::

    Level 1 for 1000pts    Score: 0pts Errors: 0/3
    What is RAM?
        1) Memory
        2) Female Sheep
        3) Baby Sheep
        4) Forgotten Sheep
    Your answer (Enter to Cancel)? 2
    WRONG! 1 Errors

    Level 1 for 1000pts    Score: 0pts Errors: 1/3
    What is RAM?
        1) Memory
        2) Female Sheep
        3) Baby Sheep
        4) Forgotten Sheep
    Your answer (Enter to Cancel)? 3
    WRONG! 2 Errors

    Level 1 for 1000pts    Score: 0pts Errors: 2/3
    What is RAM?
        1) Memory
        2) Female Sheep
        3) Baby Sheep
        4) Forgotten Sheep
    Your answer (Enter to Cancel)? 4
    WRONG! Sorry, you've lost everything

    Please try again!
    Press <enter> to leave > 

Reading the Game
----------------

You can download the game and the questions here:

* `game.py <exercises/trivia/game.py>`_
* `questions.csv <exercises/trivia/questions.csv>`_

Background
~~~~~~~~~~

* we need to be able to :doc:`openfile` to load our questions

  * we will use :doc:`loops` to load the questions from the file
  
* we will store those questions and answers (in :doc:`lists`)
* we want to pull out particular elements in the lists (via :doc:`listindexing`)

  * the first field in each line is a question
  * the second field is the answer
  * the rest of the line is wrong answers

* we want to loop over the questions (with for :doc:`loops`)
* we need to be able to define :doc:`functions` to make the code easier to understand
  
.. toctree::
   :maxdepth: 2

   lists
   listindexing
   loops
   stringmanipulation
   openfile
   functions

Overall Game Loop
------------------

Our overall game looks like this:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: run_game

We are going to track:

* score (points)
* errors (to see if the user has failed)

* we are using the `function` form of :py:func:`print` here, just to change things up

  * if you look at the top of the module you will see a weird `import` statement 
    where we imported the print function

* the current level (and level number)

  * we'll do this by iterating with a for loop (see :doc:`loop`)
  * we use the :py:func:`enumerate` function to track our current level number

But to iterate over the questions, we have to have them loaded
first.

Loading the Questions
----------------------

This is what the `questions.csv <exercises/trivia/questions.csv>`_ file looks like:

.. literalinclude:: exercises/trivia/questions.csv
    :lines: 1
    
CSV files are a common way to represent a simple spreadsheet-like grid 
of columns and rows. There's a module that handles all of the 
details of reading this format for us:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: load_questions

The only bit of extra logic is to reject short lines (the if statement that checks len( record )).

Running a Level
---------------

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: run_level

Things to investigate:

* :doc:`listindexing` (level[0], level[1], level[1:], answers[response])
* :py:func:`random.shuffle` so that the answer isn't always `1`
* `score // 2` (divide without producing a fractional number)

Randomizing the Order
~~~~~~~~~~~~~~~~~~~~~

* We *both* need to keep track of what answer is correct *and* randomize the list.
* We do that by tracking the correct answer with:

.. code-block:: python
    
    correct = level[1]

* When the user chooses a number (index) we check what `answers[chosen]` is and 
  compare that to our saved `chosen` variable
* We catch any errors where the user has chosen a number that's not in the answer 
  set (such as -112) and ask them to behave


Displaying Status/Questions
----------------------------

We are going to use the :py:class:`str` class' `.format` method to format our 
game status and questions:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: display_status
    
That's one big call, the `{0: 2d}` format inside the string reads as:

* take the first (0-th index) value
* format it with 2 spaces
* as a decimal (base-10 number)

While the `{3}` format reads as:

* take the fourth (3-rd index) value 
* format it "naturally"

We do the same thing for the questions, but we indent those lines 
(put spaces in front of them) so it's easier for the user to read them.
We're going to use the :py:func:`enumerate` function again to keep 
track of which number we are currently showing.

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: display_questions

.. note::

    Most people tend to think in 1-index numbers, so we add 1 to the 
    value we're getting from :py:func:`enumerate`.
    
Getting The User's Choice
-------------------------

* We'll use :py:func:`raw_input` to get the user's selection
* We want to allow the user to quit, so if they enter nothing (just hit enter)
  we return a None 
* We *don't* want the user hitting a wrong key to make them exit, so we catch 
  any errors trying to make the number an integer and allow them to retry

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: get_response


Calculating the Reward
-----------------------

* We use a basic point amount of 1000 and then double it for each level

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: reward

Run the Game when the Script is Run
------------------------------------

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :start-after: #mainline_start
    :end-before: #mainline_stop
