Trivia Game
===========

We are going to create a trivia game that requires:

* reading files
* text manipulation
* list iteration
* function definitions

* We will load some trivial questions from a `file`
* We will ask the user each question in turn
* If the user gets the correct answer

  * they increase their `reward`
  * the reward increases (doubles) for each question
  
* If the user gets the wrong answer, they lose all rewards and the game is over
* If the user decides to quit (enter no answer)

  * they exit with their current reward (`winning` that amount)

Before We Start
----------------

This project is far more advanced than the :doc:`guessinggame`, so we are going 
to need to cover a few ideas before we can create the game itself:

* we want to store the questions and answers in :doc:`lists`
* we want to be able to pull out particular elements in the lists via :doc:`listindexing`
* we want to be able to loop over the lists of questions with for :doc:`loops`
* we need to do :doc:`stringmanipulation` to load questions from the questions file
* we need to be able to define :doc:`functions` to make the code easier to understand
  
.. toctree::
   :maxdepth: 2

   lists
   listindexing
   loops
   stringmanipulation
   functions

Getting Set Up
--------------

Now that we know everything, we can start writing our game!
But first we need to get a copy of the questions we'll be using.

The questions are in a file at::

    \\tdsbscr11\schclass11$\1329\1329-STU\CodingClub\trivia

You should have a `High Park Student` (or `Annette Student`) link on your desktop
that will point to the directory holding the `CodingClub` folder.

Copy the `questions.txt` file to your home directory (`H:`).

.. note::

    If you are comfortable with `Windows Explorer` you can create a folder
    for CodingClub so that your work here isn't mixed up with your work
    for classes.

Reading the Questions
---------------------

A `file` on disk is just a sequence of `bytes` (a string) that we need to read
into the `interpreter` and process to make it useful.  The particular file 
we are going to read looks like this::

    Question|Right Answer|Wrong Answer|Wrong Answer
    
How do we actually get access to the bytes in the file?

.. code-block:: python

    >>> file = open('questions.txt')
    >>> file
    <open file 'questions.txt', mode 'r' at 0x7f437b5344b0>
    >>> for line in file:
    ...     print repr(line)
    'Who was the first Prime Minister of Canada?|Sir John Alexander Macdonald|Lester B. Pearson|Guglielmo Marconi|Avril Lavigne|Pierre Elliott Trudeau\n'

that is, each line in the file has a question followed by a "|" character, then 
the *correct* answer, then some number of *wrong* answers, and then a "\n" character
(which is a `new-line` `escape-code`). 

We want to turn the file into something we can work with easily (yes, those lists 
we learned about):

.. doctest::

    >>> questions = [
    ...         [ 'Question', 'Right Answer', 'Wrong Answer', 'Wrong Answer' ],
    ... ]
    >>> level = questions[0]
    >>> level
    ['Question', 'Right Answer', 'Wrong Answer', 'Wrong Answer']
    >>> level[0]
    'Question'
    >>> level[1]
    'Right Answer'
    >>> level[1:]
    ['Right Answer', 'Wrong Answer', 'Wrong Answer']

That is, we want to:

* strip off the `new-line`, which is a type of `white-space`
* `split` the `fields` into a list of strings

Stripping the `white-space` from a string is done via a `method` on the string:

.. doctest::

    >>> with_whitespace = 'Question|Right Answer|Wrong Answer|Wrong Answer\n'
    >>> with_whitespace.strip()
    'Question|Right Answer|Wrong Answer|Wrong Answer'
    >>> stripped = with_whitespace.strip()

Splitting the content of a string is done with another method. We tell the 
method to use '|' as the string to use for splitting, as otherwise it would 
default to using `white-space`.

.. doctest::

    >>> line = 'Question|Right Answer|Wrong Answer|Wrong Answer'
    >>> level = line.split('|')

Exercise: Create your Script and Read the file
----------------------------------------------

* Create a *new* game file (you can call it trivia.py) in your Home directory (`H:`).
* Copy the `questions.txt` file to the same directory if you haven't already
* For each line in the file, strip the whitespace, split into fields and print the resulting level

