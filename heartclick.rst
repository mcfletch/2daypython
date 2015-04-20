Heart Click
===========

This is going to be our first "Arcade" game, one with images
and a fast-paced mouse-based interaction:

* We are going to show an image (a heart)
* We are going to move that image around the screen
* The user needs to click on the heart with the mouse to win

First, Though, A Pink Screen
-----------------------------

.. literalinclude:: exercises/heartclick/eventloop.py
    :language: python

Loading a Heart Image
---------------------

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #load_image_start
    :end-before: #load_image_stop

How do Computers Represent Images?
++++++++++++++++++++++++++++++++++

Computer programs normally represent images as a grid of `pixels` 
where each pixel has 3 colours, Red, Green and Blue. We can combine
light from those three colours to make most hues that humans can
see.




Displaying a Heart
------------------

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #draw_image_start
    :end-before: #draw_image_stop

Checking for a Heart-Hit
------------------------

.. literalinclude:: exercises/heartclick/clickimage.py
    :language: python
    :start-after: #load_award_start
    :end-before: #load_award_stop

.. literalinclude:: exercises/heartclick/clickimage.py
    :language: python
    :start-after: #click_check_start
    :end-before: #click_check_stop
