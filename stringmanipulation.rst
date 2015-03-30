String Manipulations
====================

* strip (remove whitespace or other characters)

.. doctest::

    >>> value = '  25.3  '
    >>> value
    '  25.3  '
    >>> value.strip()
    '25.3'
    >>> quoted = '"this"'                                                                                                                             
    >>> quoted                                                                                                                                        
    '"this"'
    >>> quoted.strip('"')
    'this'
  
* split, join

.. doctest::

    >>> row = 'Silver Deer,69,-0.115,0.993,-0.12,25,violet'
    >>> components = row.split( ',' )
    >>> components
    ['Silver Deer', '69', '-0.115', '0.993', '-0.12', '25', 'violet']
    >>> print "\n".join( components )
    Silver Deer
    69
    -0.115
    0.993
    -0.12
    25
    violet
    >>> not_all_strings = [ 'Silver Goat', 45, -.333, .75, .08, 5, 'violet' ]
    >>> "\n".join( not_all_strings )
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sequence item 1: expected string, int found

* `format <http://docs.python.org/library/string.html#formatstrings>`_

.. todo:: this is *extremely* distracting, there is obvious complexity and the students get side-tracked

.. doctest::

    >>> count = 53
    >>> mean = 37.036
    >>> label = 'DMX Score'
    >>> '{0},{1},{2}'.format( label, count, mean )
    'DMX Score,53,37.036'
    >>> '{0!r} for {1} items {2:0.2f}'.format( label, count, mean )
    "'DMX Score' for 53 items 37.04"  
