Getting Input
=============

Most programs want to take some :py:func:`raw_input` to produce some output:

.. code-block:: python

    >>> raw_input( 'What is your number: ' )
    '32'
    >>> number = raw_input( 'What is your number: ' )
    >>> number 
    '32'

.. note::

    If you are using Python 3.x you need to use :py:func:`py3:input` instead of :py:func:`raw_input`.
    

Exercise
--------

* Ask yourself for a number
* Try to convert the value you enter into a `float`
