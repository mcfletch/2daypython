Heart Click ++
==============

You are going to make 1 **small** code change to your :doc:`heartclick` game.
If you'd like to work with a friend, feel free.

Quick Review
------------

This is what :doc:`heartclick` looks like...

.. code-block:: python

    # Import modules to do work for us...
    # Set up our resources
    resource = set_up_resource()
    other_resource = set_up_other_resource()
    
    # Set up the state we track
    state = create_game_state()
    
    while True: # Run until we say so 
    
        # Process user Input
        event = get_event()
        while event is not nullevent:
            if event == something_interesting:
                state = change_state(state)
        
        # Update our simulation (movement, etc)
        state = simulate( state )
        
        # Draw our game 
        clear()
        draw_game(state)
        flip()
        wait_for_next_frame()

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

* Is there anything in your plan that you don't yet know how to do?
* Can you find out how to do it from the Pygame documentation?
* Can you find out how to do it from a web search?
* Can you play around at the command-line to find the solution?

