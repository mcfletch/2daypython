Functions
=========

Functions are a way of organizing our code into maneageable pieces. They let us:

* give human-friendly names to blocks of code
* hide the details of how something works
* reuse pieces of code in multiple places

Defining a Function
--------------------

Functions are started with the keyword `def` (short for `define` a function).
All (python) functions `return` a value, even if the value they return is None.

.. code-block:: python

    def function_name():
        return "Hello Function"

    print( function_name() )

Parameters for Reuse
--------------------

Functions normally accept `parameters` that they use to control how they function.

.. code-block:: python

    def function_name( name ):
        return "Hello "+ name
    
    print( function_name( username ))

Naming and Documentation
------------------------

Choosing a friendly, easily-understood name for your functions is an art.
Documenting what they do lets users understand what your function is supposed 
to do, what it will return, and when to use it.

Each programming language has a different way of documenting functions. In 
Python we use "docstrings", which are just strings that occur on the first 
line of the function. We normally use `triple-quoted strings` so that we 
can write multiple lines of documentation.

.. code-block:: python

    def greeting( name ):
        """Adds a greeting to name
        
        returns formatted greeting as a string
        """
        return "Hello "+ name

Scoping
-------

When we pass a `parameter` into a function, we make that parameter available as
a `name` within the `namespace` of the function. The function actually operates
with multiple `namespaces` active, if a name can't be found in the `local` 
`namespace` then the next "higher" namespace is checked.  For instance:

.. code-block:: python

    outside = 3
    def add_weight( weight ):
        # outside is *not* defined in this function
        # but we can still access the value from the "global" namespace (the module)
        return weight + outside 

Default Parameters
------------------

Sometimes we want our function to have a default value for a parameter, but allow 
the user to change that parameter if they need to:

.. code-block:: python

    def greeting( name='World' ):
        """Adds a greeting to name
        
        name -- the name to greet, defaults to "World"
        
        returns formatted greeting as a string
        """
        return 'Hello '+name
    
    greeting()

