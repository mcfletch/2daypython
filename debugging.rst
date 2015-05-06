It Crashes!
===========

When we encounter failures in our code, we call them `bugs`, and 
we call the process of fixing them `debugging`.

Normally a programmer runs their program either from an IDE (such as 
PyScripter, PyDev, PyCharm, Eric, etc) or they run it from the 
command line, so that they can directly see traceback information:

.. code-block:: bash

    $ python exercises/heartclick/crash.py 
    Traceback (most recent call last):
      File "exercises/heartclick/crash.py", line 7, in <module>
        raise RuntimeError("Moo")
    RuntimeError: Moo

But since we can't do that with TDSB student accounts, we'll have 
to work around it.

Why did it crash?
-----------------

To catch the output of our script without being able to run our script from the 
command line we can do this:

.. code-block:: python

    >>> import subprocess,os
    >>> output,_ = subprocess.Popen(
    ...    ['python','h:\\heartclick.py'],
    ...    stdout=subprocess.PIPE,
    ...    stderr=subprocess.STDOUT
    ... ).communicate()
    >>> print output
    Traceback (most recent call last):
      File "exercises/heartclick/game.py", line 7, in <module>
        raise RuntimeError("Moo")
    RuntimeError: Moo

that lets us run our script and see all of its output, but *only* after the 
game exits. The :py:mod:`subprocess` module allows us to run commands as though we 
had a console.

We can also store this in a script that we can double-click:

.. code-block:: python

    import subprocess,os
    output,_ = subprocess.Popen(
        ['python','h:\\heartclick.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    ).communicate()
    print(output)
    raw_input('Hit <enter> to close: ')

    
Pause Before Crash-exit
-----------------------

We can install a "hook" in our game as :py:func:`sys.excepthook` 
so that the console doesn't just close on failures, but instead lets you read
the traceback and asks you to hit <enter> to close the console.

.. code-block:: python

    import sys
    def print_and_wait(type,value,traceback):
        sys.__excepthook__(type,value,traceback)
        raw_input("Press <enter> to close: ")
    sys.excepthook = print_and_wait

Debugging/Line by Line
----------------------
    
You can also try stepping through your game line-by-line to see what
is happening:

.. code-block:: python

    import pdb
    pdb.set_trace()

When those lines are encountered (called a `breakpoint`) the debugger
will start and let you step through your code line-by-line. The major
commands you'll want to use are:

* n -- next line
* c -- continue to run the script without pausing at each line (until the next breakpoint)
* q -- quit exit and cause the script to crash/close
* p <something> -- print out a variable

Here's what a debugging session looks like:

.. code-block:: python

    > /home/mcfletch/2daypython/exercises/heartclick/game.py(9)<module>()
    -> clock = pygame.time.Clock()
    (Pdb) n
    > /home/mcfletch/2daypython/exercises/heartclick/game.py(12)<module>()
    -> screen = pygame.display.set_mode((300, 300))
    (Pdb) n
    > /home/mcfletch/2daypython/exercises/heartclick/game.py(13)<module>()
    -> pygame.display.init()
    (Pdb) p screen
    <Surface(300x300x32 SW)>
    (Pdb) n
    > /home/mcfletch/2daypython/exercises/heartclick/game.py(21)<module>()
    -> import os
    (Pdb) 
    > /home/mcfletch/2daypython/exercises/heartclick/game.py(24)<module>()
    -> HERE = os.path.dirname(__file__)
    (Pdb) n
    > /home/mcfletch/2daypython/exercises/heartclick/game.py(27)<module>()
    -> heart_filename = os.path.join(HERE,'heart.png')
    (Pdb) p HERE
    'exercises/heartclick'
    (Pdb) q

:py:mod:`pdb` is a very basic `debugger` with simple command-line controls.

