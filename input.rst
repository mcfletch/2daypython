Getting Input
=============

Most programs want to take some input to produce some output:

.. code-block:: python

    >>> raw_input( 'What is your number: ' )
    '32'
    >>> number = raw_input( 'What is your number: ' )
    >>> number 
    '32'

.. note::

    If you are using Python 3.x you need to use `input` instead of `raw_input`.

Try it out. While you're doing it, try to convert the value the user enters into a `float`.
