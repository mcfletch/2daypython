Where are You?
==============

Try to answer the following puzzles. If you get stuck, try writing/running them.

* what does the following do?

  .. code-block:: python
  
    while True:
        print( hello world )

* what does the following do?

  .. code-block:: python
  
    while True:
        print("Hello World")

* what does the following do?

  .. code-block:: python
  
    x = 10
    while True:
        print(x)
        x = x - 1

* what does the following do?

  .. code-block:: python
  
    x = 5
    while True:
        if x > 3:
            print(x)
        x = x - 1

* what does the following do?

  .. code-block:: python
  
    x = 3
    while x > 3:
        print(x)
        x = x - 1

* what does the following do?

  .. code-block:: python
  
    x = 3
    while x < 3:
        print(x)

* what does the following do?

  .. code-block:: python
  
    x = "this"
    while x:
        print(x)
        x = x[:-1]

* what does the following do?

  .. code-block:: python
  
    x = (2,3)
    while x[0] < 5:
        x = x[0] + 1, x[1]

* what is the value of x?

  .. code-block:: python
        
    x = 32
    if x == 32:
        x = x - 4
        x = x - 4
    x = x - 4
    print(x)

* what does the following do?

  .. code-block:: python

    x = 10
    while x > 5:
        if x <= 7:
            x = x + 5
        else:
            x = x - 3
        print(x)
    
* what do these directions mean in Pygame (left, right, up, down, how fast)?

    * (-1,1)
    * (-10,20)
    * (0,10)
    * (10,1)

* what does the following do? See :doc:`heartclickfunc`

  .. code-block:: python

    def greeting(name):
        return "Hello " + name 
    print( greeting( "Mom" ))

Solving Problems
----------------

* Print *Hello World*
* Print the integers from 1 to 10
* Print every integer from 1 to 100 that is a multiple of 10 (hint, remainder is spelled `%` in Python)
* 
