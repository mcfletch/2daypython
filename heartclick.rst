Heart Click
===========

This is going to be our first "Arcade" game, one with images
and a fast-paced mouse-based interaction:

* We are going to show an image (a heart)
* We are going to move that image around the screen
* The user needs to click on the heart with the mouse to win

First, A Pink Screen
--------------------

.. literalinclude:: exercises/heartclick/eventloop.py
    :language: python

Find Our Image
--------------

We are going to save two images in the same directory as our `game.py` script:

* `heart.png <./exercises/heartclick/heart.png>`_
* `award.png <./exercises/heartclick/award.png>`_

To do so, use the right mouse-button to click on the links above. Choose 
"save link as" and save the files to the directory where you are writing 
your game (H:\).

But how do we find out *where* those files are in our `game.py` script?

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #find_image_start
    :end-before: #find_image_stop

Great, but now how do we actually get it into the game?
    
Loading an Image
----------------

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

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #load_award_start
    :end-before: #load_award_stop

.. literalinclude:: exercises/heartclick/clickimage.py
    :language: python
    :start-after: #click_check_start
    :end-before: #click_check_stop
