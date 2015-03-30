Modules
-------

* using code from other files, modules and importing
* put all code into functions
* __name__ == '__main__'

.. literalinclude:: exercises/moduledemo1.py
    :language: python

.. literalinclude:: exercises/moduledemo2.py
    :language: python

.. literalinclude:: exercises/pretty_print.py
    :language: python

Exercise
~~~~~~~~

* write a function that finds the mean of a list of numbers and use
  it to find the mean of each of the score columns in ``sample_data.csv``
* use your functions in ``readdata.py`` by importing them

  * you will need to modify ``readdata.py`` so that it doesn't print
    anything when you import it

.. literalinclude:: exercises/moduleexercise.py
    :language: python
