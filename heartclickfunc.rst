Heart Click in Functions
========================

We are going to rework :doc:`heartclick` to use :doc:`functions` to structure it 
in a clean and maintainable manner.

:doc:`heartclick` has the following basic operations:

* setup an initial set of resources (images and sounds) and state (a random direction)
* played a sound on load/startup
* then we started a loop where we:

  * updated our state (and/or exited) based on the user's actions
  * updated our state based on our simulation (motion, collisions)
  * drew the game on-screen

That suggests that each of those bullet-points should likely be their own function.
But first we need to deal with what `state` means above...

Passing Around State
---------------------

We mention `state` a lot in the description above. State here is a collection of 
bits and pieces, each of which has a name or role to play in the game. Some 
pieces of state are actually `resources` that we've loaded from disk. Some are
values we are tracking in order to update our game's simluation.

How can we pass around that state? We *could* define a separate parameter for 
each function in which to pass around each part of the state the function needed:

.. code-block:: python

    def update_simulation( direction, heart_rectangle, screen ):
        ...
        return direction, heart_rectangle
        
    direction,heart_rectangle = update_simulation( direction, heart_rectangle, screen )

but as our game-state gets more complex this is going to get rather annoying.

What we want is a data structure that lets us pass around all of the state as a 
single "thing" to which we can attach all of the various bits of state. We
could use :doc:`lists` to do this, and it would look something like this
(you'll see this a lot in low-level languages):

.. code-block:: python

    state = [ heart_image, heart_rectangle, award_image, direction, ... ]
    ...
    state[3] = state[3][1],state[3][0]

But while it would work, it's somewhat clumsy and limiting refering to individual
bits of state via indices. Low-level languages often work around that by doing 
something like this:

.. code-block:: python

    DIRECTION = 3
    ...
    state = [ heart_image, heart_rectangle, award_image, direction, ... ]
    ...
    state[DIRECTION] = state[DIRECTION][1],state[DIRECTION][0]

:doc:`dictionaries` allow us to pass around our game `state` with each bit of 
state given an easy-to-read key.  You should play with :doc:`dictionaries` a bit 
to understand how they work and what they let you do before you continue.

Refactoring into Functions
--------------------------

We want to `define` a function for each logical operation, giving the function an 
obvious name. Let's start with the function to setup our state.

.. code-block:: python
    
    def setup_state():
        state = {}
        return state

We have lots of code that is involved in setting up state, which looks like:

.. literalinclude:: exercises/heartclick/gameclean.py
    :language: python
    :start-after: #setup_state_start
    :end-before: #setup_state_stop

What does that code actually need to run?

* it uses the screen object (to convert images on load)
* it uses the value `__file__` to calculate where our resources (images, sounds) are

  * this is one of those rare cases where we likely want to use a global variable
    as the value of `__file__` truly is a static value looked up once on module 
    load.
  * we'll define a global variable `RESOURCES` that tells people reading our code 
    that we're referring to `the directory where resources are stored` rather than 
    using `HERE` directly.

So it sounds as though we should have a single parameter (screen) to our function:

.. code-block:: python

    def setup_state(screen):
        state = {}
        return state

Now we can fill in the rest of our setup_state function. Instead of storing the 
state as global variables, we are going to store the state in the state dictionary.

.. code-block:: python

    heart = pygame.image.load(heart_filename).convert_alpha(screen)
    heart_rectangle = heart.get_rect(center=(150, 150))
    # becomes
    state['heart'] = pygame.image.load(heart_filename).convert_alpha(screen)
    heart_rectangle = state['heart'].get_rect(center=(150, 150))

The whole `setup_state` function looks something like this:
    
.. literalinclude:: exercises/functions/game.py 
    :language: python
    :pyobject: setup_state

Keep Going
----------

Keep refactoring your :doc:`heartclick` game into a set of functions.

Sample Solution
---------------

.. literalinclude:: exercises/functions/game.py 
    :language: python

When you're done, continue with :doc:`heartclickplusplus`.
