Reading a File
==============

* look at ``../sample_data.csv``, note how it looks like the data in the
  previous exercise
  
.. literalinclude:: sample_data.csv 

* this is a standard comma separated value data-file, possibly from some survey
  which observed animals and subjected them to various (humane) tests which 
  generated measurements.  Let's poke around in it:

.. doctest::
  
    >>> reader = open( '../sample_data.csv', 'r') # r is for "read" mode
    >>> reader #doctest: +ELLIPSIS
    <open file '../sample_data.csv', mode 'r' at 0x...>
    >>> content = reader.read()
    >>> len(content) 
    995
    >>> reader.close()
    >>> lines = content.splitlines()
    >>> len(lines)
    21
    >>> lines[0]
    'Subject,Count,DMX Score,Coda Score,Vinny Score,Zim Score,Subject Choice'
    >>> lines[1]
    'Dodgerblue Lemming,30,-0.988,0.154,-6.41,36,yellow'
    >>> lemming = lines[1]
    >>> columns = lemming.split(',')
    >>> columns
    ['Dodgerblue Lemming', '30', '-0.988', '0.154', '-6.41', '36', 'yellow']
    >>> measurement = columns[2]
    >>> measurement
    '-0.988'
    >>> type(measurement)
    <type 'str'>
    >>> measurement = float( measurement )
    >>> measurement
    -0.988
    >>> type(measurement)
    <type 'float'>

* the previous loaded the whole file into memory at one go, we could also 
  have iterated over the file line-by-line.
  
.. doctest::

    >>> reader = open( '../sample_data.csv', 'r')
    >>> header = reader.readline()
    >>> header # note the '\n' character, you often need to do a .strip()!
    'Subject,Count,DMX Score,Coda Score,Vinny Score,Zim Score,Subject Choice\n'
    >>> for line in reader:
    ...     print float(line.split(',')[2])
    ... 
    -0.988
    0.035
    ...

* the special file ``sys.stdin`` can be used to process input which is being 
  piped into your program at the ``bash`` prompt.

.. literalinclude:: exercises/argumentsstdin.py
    :language: python

.. code-block:: bash 

    $ cat ../sample_data.csv | ./argumentsstdin.py 
    -0.988
    0.035
    -0.898
    0.913
    ...

.. note::

  file objects keep an internal "pointer" (offset, bookmark) which they
  advance as you iterate through the file.  Regular files on the 
  file-system can be "rewound" or positioned explicitly.  File-like 
  objects such as pipes often cannot provide this functionality.

    
Exercise
~~~~~~~~

* read data from ``../sample_data.csv`` so that you have a list of strings,
  one string for each line in the file
* use code from ``dictexercise.py`` to again map names to colours and
  print the colour of a "Firebrick Coyote"
* use code from ``iterexercise.py`` to turn data into columns and
  find out which animal was spotted most frequently

.. literalinclude:: exercises/filereadexercise.py
    :language: python

