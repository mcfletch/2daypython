Trivia Game
===========

Our second game is a Trivia Game that works like so:

* We load some trivial questions
* We ask the user each question in turn
* If the user gets the correct answer

  * they increase their `reward`
  * the per-question reward increases (doubles) for each question
  * the reward accumulates (adds to the current value) for each question
  
* If the user gets the wrong answer, they lose all rewards and the game is over
* If the user decides to quit (enter no answer)

  * they exit with their current reward (`winning` that amount)
  
What it Looks Like
------------------

This is what running the game should look like::

    Level 1 for $1000    Current winnings: $0
    Who was the first Prime Minister of Canada?
        1) Avril Lavigne
        2) Guglielmo Marconi
        3) Sir John Alexander Macdonald
        4) Pierre Elliott Trudeau
        5) Lester B. Pearson
    Your answer? 3
    Level 2 for $2000    Current winnings: $1,000
    What is the captial of Nunavut?
        1) Iqaluit
        2) Montreal
        3) St. Johns
        4) Alaska
        5) Red Deer
    Your answer? 4
    Sorry, the correct answer was: Iqaluit
    Please try again!

And this is what the questions look like:

.. literalinclude:: exercises/trivia/questions.txt


Code Walk Through
------------------

Running the Game:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: run_game

Loading the Questions from a file:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :start-after: #read_file_start
    :end-before: #read_file_stop

Displaying Status:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: display_status

Displaying Question and Shuffled Answers

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: display_questions
    
Getting User's Choice:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: get_response

Calculating the Reward for each Level:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :pyobject: reward

Run the Game when the Script is Run:

.. literalinclude:: exercises/trivia/game.py
    :language: python
    :start-after: #mainline_start
    :end-before: #mainline_stop

Getting Set Up
--------------

We'll be reading our trivia questions from a file. The file is here:

    `questions.txt <./exercises/trivia/questions.txt>`_

Copy the `questions.txt` file to your home directory (`H:`).

.. note::

    If you are comfortable with `Windows Explorer` you can create a folder
    for CodingClub so that your work here isn't mixed up with your work
    for classes.
    
  
Before We Start
----------------

This project is far more advanced than the :doc:`guessinggame`, so we are going 
to need to cover a few ideas before we can create the game itself:

* we need to be able to :doc:`openfile` to load our questions

  * we will use :doc:`loops` to load the questions from the file
  * we will do :doc:`stringmanipulation` to load questions from the questions file
  
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

Breaking Down the Game (Psuedo-code)
------------------------------------

Now that we know everything, we can start writing our game!

.. code-block:: python

    def run_game():
        levels = load_questions()
        for level_number in range(len(levels)):
            level = levels[level]
            display_questions(level)
            choice = get_response()
            if is_right( choice ):
                add_reward()
            else:
                reward = 0
                break
        print_final_reward()

There are problems there:

* how does the user know how much reward each level is?
* how does the user know how much they have earned so far?
* how are we tracking those amounts?
* how do we calculate the reward for each level?

.. code-block:: python

    def calculate_reward(level_number):
        ...
    def run_game():
        levels = load_questions()
        winnings = 0
        for level_number in range(len(levels)):
            level = levels[level]
            display_status( level_number, winnings )
            display_questions(level)
            choice = get_response()
            if is_right( choice ):
                winnings += calculate_reward(level_number)
            else:
                reward = 0
                break
        print_final_reward()

* how do we display the answers in a format where the answer isn't always the first choice?

  * hint :py:func:`random.shuffle`
  * we need to *save* the particular order so we can check if the user got it right

Load Questions
--------------

We saw how to :doc:`openfile`, now we're going to work out how to read the 
content of the file into a list-of-lists-of-strings that we can actually use
to run the game (using :doc:`stringmanipulation`).

Our questions are stored in a simple plain-text file::

    Question|Right Answer|Wrong Answer|Wrong Answer
    Question|Right Answer|Wrong Answer|Wrong Answer

We want to turn the file into something we can work with easily (:doc:`lists`):

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


When we read in a line from the file, we get something like::

    'Question|Right Answer|Wrong Answer|Wrong Answer\n'

That '\n' character is a `new-line` code which is what actually defines
the end of a line in a `file`, but it's not very useful for us, so 
we want to:

* strip off the `new-line`, (which is a type of `white-space`)
* `split` the `fields` of each line into a list of strings

Recall from :doc:`stringmanipulation` that we have a method `strip` on strings:

.. doctest::

    >>> with_whitespace = 'Question|Right Answer|Wrong Answer|Wrong Answer\n'
    >>> with_whitespace.strip()
    'Question|Right Answer|Wrong Answer|Wrong Answer'
    >>> stripped = with_whitespace.strip()

Similarly, from :doc:`stringmanipulation` we also have a method `split` on strings.
We need to pass a `parameter` (from :doc:`functions`) to the method to tell it 
what character to use for splitting. If we didn't provide that parameter it would
split on `white-space`.
    
.. doctest::

    >>> line = 'Question|Right Answer|Wrong Answer|Wrong Answer'
    >>> line.split()
    ['Question|Right', 'Answer|Wrong', 'Answer|Wrong', 'Answer']
    >>> level = line.split('|')

We want to collect *all* of the levels (lines) into a `list-of-levels`
that we can use in the game:

.. doctest::

    >>> levels = []
    >>> file_handle = open('trivia/questions.txt')
    >>> def read_line( line ):
    ...     return line.strip().split('|')
    >>> for line in file_handle:
    ...     levels.append( read_line(line) )
 
And finally, we want to put all of that into a :doc:`functions` with a name that tells 
us what the function does for us and lets us specify :

.. code-block:: python

    def load_questions( ):
        """Loads our questions from questions.txt
        
        returns
        
            [ [ Question, Answer, Wrong Answers ], ... ]
        """
        return ...


Exercise: Create your Script and Read the Questions
+++++++++++++++++++++++++++++++++++++++++++++++++++

* Create a *new* game file (you can call it trivia.py) in your Home directory (`H:`).
* Copy the `questions.txt` file to the same directory if you haven't already
* For each line in the file, strip the whitespace, split into fields and print the resulting level

