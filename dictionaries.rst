Dictionaries
============

* a.k.a. hash-tables in other languages, have special syntax in most scripting 
  languages

  * keys must be immutable (technically, hashable)
  * values (anything)

.. literalinclude:: exercises/dictdefinitions.py
    :language: python

* you can add, remove, reassign

.. doctest::

    >>> dictionary = {}
    >>> dictionary
    {}
    >>> dictionary['this'] = 'those'
    >>> dictionary
    {'this': 'those'}
    >>> dictionary['those'] = 23
    >>> dictionary
    {'this': 'those', 'those': 23}
    >>> len(dictionary)
    2
    >>> dictionary['this'] == 'those'
    True
    >>> del dictionary['those']
    >>> dictionary
    {'this': 'those'}
    >>> 'those' in dictionary
    False
    >>> 'this' in dictionary
    True
    >>> dictionary['those']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'those'

* only one entry for each equal-hash-and-compare-equal key

  * you can thus use a dictionary to confirm/create uniqueness
  * values *must* compare equal *and* have the same "hash", this is 
    "computer equal", not "human equal", though Python tries to make 
    "computer equal" a bit more human e.g. with floats/ints

.. doctest::
  
    >>> dictionary = {'this':'that'}
    >>> dictionary[ ' this ' ] = 'thar'
    >>> dictionary
    {'this': 'that', ' this ': 'thar'}
    >>> dictionary[ 45 ] = 8
    >>> dictionary[ 45.0 ] = 9
    >>> dictionary
    {'this': 'that', ' this ': 'thar', 45: 9}
    >>> # Super Bonus Ask During Coffee Question: why is the key 45 and not 45.0?
    
* iterable, but un-ordered, so don't depend on the order of items 

.. literalinclude:: exercises/dictiteration.py
    :language: python
  
Exercise
~~~~~~~~

* loop over a list of strings, split into key: value pairs and add to dictionary

.. literalinclude:: exercises/dictexercise.py
    :language: python
