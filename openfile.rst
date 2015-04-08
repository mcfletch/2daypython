Read a File
===========

* files are `strings` that are stored on `disk`
* we normally access them by using a `path` which describes their location
* to work with the strings inside we use the `open` function:

.. doctest::

    >>> path = 'trivia/questions.txt'
    >>> file_handle = open( path, 'r')
    >>> file_handle
    <open file 'trivia/questions.txt', mode 'r' at ...>

* we can treat a file like a `list` of lines (in some ways)

    >>> for line in file_handle:
    ...    print repr(line)
    'Who was the first Prime Minister of Canada?|Sir John Alexander Macdonald|Lester B. Pearson|Guglielmo Marconi|Avril Lavigne|Pierre Elliott Trudeau\n'
    ...
    >>> for line in file_handle:
    ...    print repr(line)
    >>> # HUH? why not?

* the file has a `position` and as you `iterate` over it that position moves through the file

Exercise: Iterate Over a File
------------------------------

* Create a new script that opens your `questions.txt` file and just prints every line
* Why are there blank lines?
* Modify your script to *not* show blank lines (hint :doc:`stringmanipulation`)
