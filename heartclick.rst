Heart Click
===========

This is going to be our first "Arcade" game, one with images
and a fast-paced mouse-based interaction:

* We are going to show an image (a heart)
* We are going to move that image around the screen
* The user needs to click on the heart with the mouse to win

(Let's see what the finished game will look like)...

.. note::

    This is going to take a few weeks, likely.
    Don't expect to finish the whole game today.
    If you are feeling lost, feel free to work with a friend.

First, A Pink Screen
--------------------

You can `download this file <./exercises/heartclick/eventloop.py>`_ .
To do that, use the **right-hand** mouse-button to click on the link. 
Choose "Save Link As" and save the file to your H:\ drive.
We are going to walk through what's going on in the file so you 
understand how an "event loop" works.

.. literalinclude:: exercises/heartclick/eventloop.py
    :language: python

If we save and run this file, we'll see an empty pink window.

Our game works like this:

* we loop forever and for every trip round the loop
* we check to see if the user has done anything and update our "model" of the game

  * currently we just check to see if they asked us to exit

* we "render" the game into memory
* we "flip" the rendered game board onto the screen (make it visible)

Adding a Heart
--------------

We need to draw a heart, so we need to get an image of a heart to draw.
We are going to save two images in the same directory as our `game.py` script:

* `heart.png <./exercises/heartclick/heart.png>`_
* `award.png <./exercises/heartclick/award.png>`_

To do so, use the **right-hand** mouse-button to click on the links above. Choose 
"Save Link As" and save the files to the directory where you are writing 
your game (on your H:\ drive).

.. image:: images/directory.png
 :alt: Image showing directory tree for the heartclick game
 
But how do we find out *where* those files are for our game?
When we run a script we get a `__file__` variable defined
which points to the module which is being run (in our case,
this is the script `game.py`).

This script just prints out the directory where the Python file is saved:

.. literalinclude:: exercises/heartclick/whereami.py
    :language: python

So how do we go from "the name of the python game file" to 
"the name of an image sitting next to the python game file"?

.. doctest::

    >>> import os
    >>> filename = '/path/to/filename.py'
    >>> os.path.dirname(filename)
    '/path/to'
    >>> HERE = os.path.dirname(filename)
    >>> os.path.join( HERE, 'heart.png' )
    '/path/to/heart.png'

So in our game, we want to modify the game-setup code to 
find the `heart.png` file:
    
.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #find_image_start
    :end-before: #find_image_stop

Great, but now how do we actually use the image file in our game?
We are going to use the `pygame.image` library's `load` function 
to open the image filename and give us an image "object" that 
we can use to draw the image onto the screen.

.. doctest::

    >>> import pygame.image
    >>> image = pygame.image.load('heartclick/heart.png' )
    >>> image
    <Surface(32x32x32 SW)>

So what we got out of that `pygame.image.load` call is a `Surface <https://www.pygame.org/docs/ref/surface.html#pygame.Surface>`_
that we can copy onto the `screen` (also a Surface). Let's see what we can do with our Surface:

.. doctest::

    >>> dir(image) # doctest: +ELLIPSIS
    [...'blit', 'convert', 'convert_alpha', 'copy', 'fill',... 'get_at', ... 'get_height', ...'get_rect', ...'get_size', 'get_width',... 'set_at', ...]
    >>> image.copy()
    <Surface(32x32x32 SW)>
    >>> image.get_size()
    (32, 32)
    >>> image.get_at((0,0))
    (0, 0, 0, 0)

We'll add this to the game setup area of our game:
    
.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #load_image_start
    :end-before: #load_image_stop

.. note:: Why .convert_alpha(screen)?

    You will note that we called `convert_alpha` on the thing we 
    loaded from the file. We did that in order to make the image 
    `compatible` with the screen onto which we will be drawing.

.. note:: :doc:`images`

    
Where To Draw
+++++++++++++

When we ask the computer to put the image of the heart onto the 
screen, we need to tell it **where** to copy the image. With Pygame
we do that by getting a `rectangle` into which we will copy the image.
We can move the rectangle around to move where we will copy the image.

Let's play with a `rectangle <https://www.pygame.org/docs/ref/rect.html>`_ a bit to see what they can do:

.. doctest::

    >>> rectangle = image.get_rect()
    >>> rectangle
    <rect(0, 0, 32, 32)>
    >>> dir(rectangle) # doctest: +ELLIPSIS
    [...'bottom', 'bottomleft', 'bottomright', 'center', 'centerx', 'centery', 'clamp', 'clamp_ip', 'clip', 'collidedict', 'collidedictall', 'collidelist', 'collidelistall', 'collidepoint', 'colliderect', 'contains', 'copy', 'fit', 'h', 'height', 'inflate', 'inflate_ip', 'left', 'midbottom', 'midleft', 'midright', 'midtop', 'move', 'move_ip', 'normalize', 'right', 'size', 'top', 'topleft', 'topright', 'union', 'union_ip', 'unionall', 'unionall_ip', 'w', 'width', 'x', 'y']
    >>> rectangle.center = (150,150)
    >>> rectangle
    <rect(134, 134, 32, 32)>
    >>> rectangle.left = 0
    >>> rectangle
    <rect(0, 134, 32, 32)>
    >>> rectangle.bottom = 300
    >>> rectangle
    <rect(0, 268, 32, 32)>
    >>> rectangle.collidepoint( (1,268))
    1
    
That last call to `collidepoint` is asking the rectangle "is this point inside you?"
and it returns `1`, a True value.

.. doctest::

    >>> rectangle.move( (10,10) )
    <rect(10, 278, 32, 32)>
    >>> rectangle
    <rect(0, 268, 32, 32)>

That last one creates a *new* rectangle, it doesn't change the rectangle
itself.  We could have used `move_ip` if we wanted to change the original
rectangle.

We'll put this into the game-setup area of the game to calculate the 
initial rectangle for the heart.

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #get_rectangle_start
    :end-before: #get_rectangle_stop

Drawing (Blitting) the Image
++++++++++++++++++++++++++++

To draw an image (Surface) on another Surface (such as the screen)
we ask the thing we want to draw onto to `blit <https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit>`_ 
(copy) the image onto itself::

    screen.blit( image, area=rectangle )

This has screen copy the pixels from image into the coordinates 
represented by rectangle. Because we are using an image with 
transparency, the pixels in `image` are blended into the pixels
currently on the screen, rather than overwriting them completely.
    
This is going to go into the game just after we fill the screen (the call to `screen.fill`):

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #draw_image_start
    :end-before: #draw_image_stop


Checking for a Heart-Hit
------------------------

Before we start moving the heart around, let's make it possible to 
win the game. We want to see if the user has clicked the mouse
inside the rectangle where we are currently drawing the heart
(`heart_rectangle`).

We will put this just after we check to see if the user has asked 
us to exit/quit:

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #click_check_start
    :end-before: #click_check_stop

So now we know that the user has successfully hit the heart,
but how do we tell the user that they've won?

Rewarding the User
++++++++++++++++++
    
We need some way to tell the user that they've won, for 
now we'll just change the "heart" into an "award" and display
that. If you didn't download it yet, do so now:

* `award.png <./exercises/heartclick/award.png>`_

We'll modify the game-setup code to load the `award.png` file
in exactly the same way as we loaded `heart.png`, from a file 
sitting next to our game.
    
.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #load_award_start
    :end-before: #load_award_stop

To draw the award, we just make the name "heart" point at the 
image we loaded into the name "award":
    
.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #show_award_start
    :end-before: #show_award_stop

Now every time we go to render "heart" we will actually be rendering
"award". Because the images are the same size, we can use the 
"heart_rectangle" to blit the award without changing any other code.

Moving the Heart
----------------

.. image:: images/cartesian.png
    :alt: Diagram showing cartesian coordinate system

So to move the heart, we need to change its x and y coordinate,
with the size of the x and y change being its "vector" of motion.

If the numbers are negative, the heart will move up/left, if they 
are positive, it will move down/right. The larger they are, the 
faster the heart will move.

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #motion_setup_start
    :end-before: #motion_setup_stop

.. topic:: Tuples

    That ( <random>, <random> ) thing is a *tuple*, which is a 
    simple thing that can hold some number of other things.
    Python programmers often use them to hold together simple pieces 
    of information that are related to each other.
    
    We can pull information *out* of a tuple by "indexing" into 
    the tuple with square brackets.
    
    .. doctest::
    
        >>> direction = (1,2)
        >>> direction[0]
        1
        >>> direction[1]
        2
    
    Or by unpacking the tuple into separate variables:
    
    .. doctest::
    
        >>> direction = (1,2)
        >>> x,y = direction

Okay, so how do we actually get the rectangle to move?
We ask the rectangle to "move" itself with its 
`move method <https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move>`_.

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #update_motion_start
    :end-before: #update_motion_stop

Bouncing Heart
--------------

It's not a very fun game if the heart goes off-screen in
a second. We need to make the heart bounce when it hits the 
edge of the screen.

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #bounce_start
    :end-before: #bounce_stop

The call to `heart_rectangle.clamp <https://www.pygame.org/docs/ref/rect.html#pygame.Rect.clamp>`_ tells the rectangle to 
create a new rectangle that is entirely *inside* the screen's
rectangle (so that the heart cannot go off-screen).

Randomizing Motion
------------------

Now the game is a bit too easy, so let's add a bit of randomness
to the heart's motion:

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #random_motion_start
    :end-before: #random_motion_stop

Exiting on Winning
------------------

As well as changing the heart to an award, we could exit the 
game when the user wins. Pygame's time module has `set_timer <https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer>`_
that lets us schedule an event to be sent after a given number 
of milliseconds (one-one-thousandth of a second).

We want to send the `pygame.QUIT` event after 1.5 seconds, which is
1500 milliseconds.

.. literalinclude:: exercises/heartclick/clickimage.py
    :language: python
    :start-after: #timer_exit_start
    :end-before: #timer_exit_stop

Audio Prompts
-------------

Instead of just exiting silently, we could play a congratulations 
and exit when that finishes. Here are some audio-prompts you can use to start:

* `clicktowin.ogg <exercises/heartclick/clicktowin.ogg>`_
* `youwin.ogg <exercises/heartclick/youwin.ogg>`_

Let's look at the process for loading an audio file:

.. doctest::

    >>> import pygame.mixer
    >>> pygame.mixer.init()
    >>> instructions = pygame.mixer.Sound('heartclick/clicktowin.ogg')
    >>> dir(instructions)# doctest: +ELLIPSIS
    [...'fadeout', 'get_buffer', 'get_length', 'get_num_channels', 'get_volume', 'play', 'set_volume', 'stop']
    >>> instructions.get_length() # doctest: +ELLIPSIS
    1.51...
    
You can record your own prompts with Audacity (or any other 
program that can save .wav or .ogg files).

.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #audio_prompts_start
    :end-before: #audio_prompts_stop

Modify the "when the user wins" section to play the `youwin.ogg` file
and exit when it finishes playing.

.. code-block::

    >>> help(instructions.play) # doctest: +ELLIPSIS
    ...Sound.play(loops=0, maxtime=0, fade_ms=0): return Channel...

So playing the sound returns a `Channel <https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Channel>`_
which has a method called `set_endevent <https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Channel.set_endevent>`_ 
that will make the channel send an event when we have finished playing
the sound. We'll use it to send the pygame.QUIT event so that the game
will exit as though the user had hit the `close` button on the window.
    
.. literalinclude:: exercises/heartclick/game.py
    :language: python
    :start-after: #audio_award_start
    :end-before: #audio_award_stop

Final Sample Code
-----------------

You can download the full source code for the game, including 
audio prompts:

* `game.py <exercises/heartclick/game.py>`_
* `heart.png <exercises/heartclick/heart.png>`_
* `award.png <exercises/heartclick/award.png>`_
* `clicktowin.ogg <exercises/heartclick/clicktowin.ogg>`_
* `youwin.ogg <exercises/heartclick/youwin.ogg>`_

.. literalinclude:: exercises/heartclick/gameclean.py
    :language: python

Documentation
-------------

* `Pygame Documentation <http://www.pygame.org/docs/>`_
* `Making Games with Python and Pygame <https://inventwithpython.com/pygame/chapters/>`_
* `Invent with Python <https://inventwithpython.com/chapters/>`_
* :doc:`installation`
* :doc:`debugging`
    
Ideas
-----

Modify your game to:

* Use different images or audio prompts

  * For example: http://webtoys.vrplumber.com/saywhat?words=You+rock&format=ogg
    
* Over time, make the heart move faster, or change direction more frequently
* Define a "no win" situation (took too long, or clicked too many times)
