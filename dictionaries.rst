Dictionaries
============

Dictionaries are things that "map" from one thing (called a key) to another
(called a value). They are (along with :doc:`lists` one of the most common 
`data structures` you will see when programming. 
They are best understood by playing with them:

Creating Dictionaries 
---------------------

.. code-block:: python

    >>> {}
    {}
    >>> {
    ...    'thar': 'thusly',
    ...    'them': 'tharly',
    ... }
    {'thar': 'thusly', 'them': 'tharly'}
    >>> {2:3, 4:None, 5:18}
    {2: 3, 4: None, 5: 18}

Adding, Accessing Keys
----------------------
    
.. doctest::

    >>> dictionary = {}
    >>> dictionary
    {}
    >>> dictionary['this'] = 'those'
    >>> dictionary['this']
    'those'
    >>> len(dictionary)
    1
    >>> dictionary['those'] = 'moo'
    >>> len(dictionary)
    2
    >>> dictionary['those'] = 'zoo'
    >>> len(dictionary)
    2
    >>> dictionary['those']
    'zoo'
    >>> dictionary['those'] + 'who'
    'zoowho'

Deleting Keys 
--------------

.. doctest::

    >>> dictionary = {"this": 23}
    >>> dictionary 
    {'this': 23}
    >>> del dictionary["this"]
    >>> dictionary 
    {}

Checking for Keys
------------------

You can use the phrase `x in dictionary` to check if a given key 
is in a dictionary. You can also just try to access the key and 
get an exception if it's not there.

.. doctest::

    >>> dictionary = {'this': 'those'}
    >>> 'this' in dictionary 
    True 
    >>> 'that' in dictionary
    False
    >>> dictionary['moo']
    Traceback (most recent call last):
      File "/usr/lib/python2.7/doctest.py", line 1315, in __run
        compileflags, 1) in test.globs
      File "<doctest default[3]>", line 1, in <module>
        dictionary['moo']
    KeyError: 'moo'

Key Matching
------------

* just like a `name` in a namespace, there's only one value assigned 
  to a given key in a dictionary
* if you assign a *new* value to that key, then the old value is 
  "lost"
  
.. doctest::

    >>> dictionary = {'a':1}
    >>> dictionary
    {'a': 1}
    >>> dictionary['a'] = 2
    >>> dictionary
    {'a': 2}

* keys *must* compare equal *and* have the same "hash"

.. doctest::

    >>> dictionary = {1:'hello'}
    >>> dictionary
    {1: 'hello'}
    >>> dictionary[1.0] = "world" # 1 == 1.0
    >>> dictionary
    {1: 'world'}
    >>> dictionary['1'] = "egads" # '1' != 1
    >>> dictionary
    {1: 'world', '1': 'egads'}

.. note::

    Why was that key still `1` instead of `1.0` when we set the key `1.0` to "world"?
    
    Internally the dictionary is a set of things that look like:
    
        hash: [(key,value),...]
    
    when you assign to an existing key that has the same hash and compares equal the 
    dictionary re-uses the (key,value) record and just assigns the new value to the 
    "value" part of it. It's an optimization that makes the dictionary object faster.

* iterable, but un-ordered, so don't depend on the order of items 

.. literalinclude:: exercises/dictiteration.py
    :language: python

Namespaces
----------

Python's `names` are (in the common implementation) actually implemented 
with dictionaries. You can see this using the :py:func:`eval` function, 
where you can run code using a dictionary as the `namespace` in which the code 
will be `evaluated`.

.. doctest::

    >>> dictionary = {'a':1,'b':2}
    >>> eval( 'a+b',dictionary)
    3
