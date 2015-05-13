Heart Click ++
==============

You can do this project *either* starting from either of:

* :doc:`heartclick`
* :doc:`heartclickfunc` 

You are going to make 1 **small** code change to your game.
If you'd like to work with a friend, feel free.

Quick Review
------------

:doc:`heartclick` had a core pattern that looked like this:

* setup an initial set of resources (images and sounds) and state (a random direction)
* played a sound on load/startup
* then we started a loop where we:

  * updated our state (and/or exited) based on the user's actions
  * updated our state based on our simulation (motion, collisions)
  * drew the game on-screen

Which in code, looked like this:

.. literalinclude:: exercises/functions/game.py
    :language: python
    :pyobject: main
    :end-before: #main_call_start

.. note::

    The function above is from the :doc:`heartclickfunc` tutorial,
    if you're curious how it works you can follow through that tutorial 
    before starting this one.

Your Idea
----------

What do you want to change about the game? Make it something small and 
simple, something you can describe in a couple of words:

* "the heart runs away from their mouse"
* "show the number of times they've clicked"
* "they lose if they click more than 10 times"
* "the heart gets faster the longer they play"
* "20 hearts"
* "2 hearts, one loses, the other wins"

When you've got your idea, add it to the Idea Board with your name.

Breaking Down the Idea
-----------------------

What do you need to change?

* Do you need to set up a resource (images, audio, fonts (for text))?
* Do you need to process user input (mouse clicks, keyboard hits)?
* Do you need to track some state (number of clicks)?
* Do you need to change how the `simulation` works (motion, etc)?
* Do you need to change how the game is drawn?

What **Don't** You Know Yet?
----------------------------

We've only covered a *tiny* fraction of programming (and Python) so far,
there are going to be *lots* of things you don't know about yet. Yay!

* Can you find out how to do it from the `Pygame Documentation <http://www.pygame.org/docs/>`_?
* Can you find out how to do it from a `web search <https://www.google.ca>`_?
* Can you play around at the command-line to find the solution?

.. code-block:: python

    >>> import pygame.font
    >>> help(pygame.font)

* You can also ask me, but that's not as much fun.
* You can read on your own, particularly you may wish to read about:

  * :doc:`dictionaries`
  * :doc:`lists`
  * :doc:`functions`
  * :doc:`loops`
