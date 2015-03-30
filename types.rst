Types
=====

.. doctest::

    >>> count = 36
    >>> print count
    36
    >>> count / 10 # surprising?
    3
    >>> irrational = 3.141592653589793
    >>> irrational
    3.141592653589793
    >>> label = "irrational, 'eh"
    >>> label2 = 'count "this"'
    >>> label3 = '''python has these too\n'''
    >>> label4 = """but they are just a different way to write the same thing"""
    >>> print label, label2, label3, label4
    irrational, 'eh count "this" python has these too
    but they are just a different way to write the same thing
    >>> print label + label2
    irrational, 'ehcount "this"
    >>> None # doesn't show up
    >>> print None
    None
    >>> print True
    True
    >>> print False
    False
    >>> True == 1
    True
    >>> False == 1
    False
    >>> False == 0
    True

* what `type` of object is something?

.. doctest::

    >>> type( 0 )
    <type 'int'>
    >>> type( 1 )
    <type 'int'>
    >>> type( 1.0 )
    <type 'float'>
    >>> type( [] )
    <type 'list'>
    >>> type( False )
    <type 'bool'>
    >>> type( 'blue' )
    <type 'str'>

.. note::

    What do those `()` characters mean in `type(0)`?
    
    We are asking a "thing" ("object") called `type` to "act" upon a single thing,
    which is our integer value `0`.
    The thing `type` has a piece of code (a "function" or "method")
    that tells it what to do when it is "asked to act" ("called") 
    on a set of things ("arguments" or "parameters").
    Here the set of arguments we are passing is a single value, but later on we will 
    see how to pass multiple arguments into functions which support multiple arguments.
    
    We'll see how to write our own functions later in this tutorial.
    A "method" is a function which is "attached" to an object, we'll use these 
    throughout the tutorial, but this tutorial does not yet cover how to write 
    our own objects.
    
