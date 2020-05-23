Getting Input
=============

Most programs want to take some :py:func:`input` to produce some output:

.. code-block:: python

    >>> input( 'What is your number: ' )
    '32'
    >>> number = input( 'What is your number: ' )
    >>> number 
    '32'

.. note::

    If you are using Python 2.x you need to use :py:func:`py2:raw_input` instead of :py:func:`input`.
    

Exercise
--------

* Ask yourself for a number
* Try to convert the value you enter into a `float`
