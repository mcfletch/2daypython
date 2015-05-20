Checkup: Where are You?
=======================

Getting Un-stuck:

* try to solve the problem

  * if you're just heading off to do surveys or play games you likely aren't 
    going to figure out how to code anything
  * ask me, ask your friends, but keep **trying**
  * there's only 4 hours left in the club this year
  
* you don't have to wait for coding club to code see :doc:`installation`
* reading is pretty important... if you're **not reading**, 
  you're **not going to understand** the instructions here
  
  * if you are having trouble with reading, we may need to switch you to a 
    graphical coding environment for now, please see me
  * programmers actually spend a *lot* of time reading, it's the only way 
    to figure out how things work much of the time

* there are other ways to learn to code see :doc:`links`
    
Puzzles
--------

Try to answer the following puzzles. If you get stuck, try writing/running them,
if you still don't understand, read and/or ask me. If you don't get these 
ideas you're going to get lost!  Getting lost can be fun, but it's more 
fun if you're lost in an interesting area.

* what does the following do? See :doc:`loops` and :doc:`guessinggame`

  .. code-block:: python
  
    while True:
        print( hello world )

* what does the following do? See :doc:`loops` and :doc:`guessinggame`

  .. code-block:: python
  
    while True:
        print("Hello World")

* what does the following do?  See :doc:`loops` and :doc:`guessinggame`

  .. code-block:: python
  
    x = 10
    while True:
        print(x)
        x = x - 1

* what does the following do?  See :doc:`loops` and :doc:`booleantests`

  .. code-block:: python
  
    x = 5
    while True:
        if x > 3:
            print(x)
        x = x - 1

* what does the following do? See :doc:`loops`

  .. code-block:: python
  
    x = 3
    while x > 3:
        print(x)
        x = x - 1

* what does the following do? See :doc:`loops`

  .. code-block:: python
  
    x = 3
    while x < 3:
        print(x)
    x = 2
    print(x)

* what is the value of x? See :doc:`booleantests`

  .. code-block:: python
        
    x = 32
    if x == 32:
        x = x - 4
        x = x - 4
    x = x - 4
    print(x)

* what does the following do? See :doc:`loops` and :doc:`booleantests`

  .. code-block:: python

    x = 10
    while x > 5:
        if x <= 7:
            x = x + 5
        else:
            x = x - 3
        print(x)
    
* what do these directions mean in Pygame (left, right, up, down, how fast)? See :doc:`heartclick`

    * (-1,1)
    * (-10,20)
    * (0,10)
    * (10,1)

* what does the following do? See :doc:`heartclickfunc` and :doc:`functions`

  .. code-block:: python

    def greeting(name):
        return "Hello " + name 
    print( greeting( "Mom" ))

* what does the following do? See :doc:`lists` and :doc:`listindexing`

  .. code-block:: python

    x = [1,2,3,4]
    print(x[2])

* what does the following do? See :doc:`lists` and :doc:`listindexing`

  .. code-block:: python

    x = [0,1,2,3,4]
    print(x[2])
    
* what does the following do? See :doc:`lists` and :doc:`listindexing`

  .. code-block:: python

    x = [0,1,2,3,4]
    print(x[2:])

* what does the following do? See :doc:`listindexing`

  .. code-block:: python
  
    x = (2,3)
    while x[0] < 5:
        x = x[0] + 1, x[1]

* what does the following do? See :doc:`loops`

  .. code-block:: python

    x = [0,1,2,3,4]
    for number in x:
        print( x * 2 )

* what does the following do?  See :doc:`lists` and :doc:`listindexing`

  .. code-block:: python

    x = [(0,'first'),(1,'second'),(2,'third'),(3,'fourth')]
    for record in x:
        print( record )

* what does the following do?  See :doc:`lists` and :doc:`listindexing`

  .. code-block:: python

    x = [(0,'first'),(1,'second'),(2,'third'),(3,'fourth')]
    for number,label in x:
        print( label )
        print( number )
    
* what does the following do? See :doc:`listindexing` 

  .. code-block:: python
  
    x = "this"
    while x:
        print(x)
        x = x[:-1]

* what does the following do? See :doc:`dictionaries` and :doc:`heartclickfunc`

  .. code-block:: python
  
    import pygame.image
    state = { }
    state['direction'] = (2,3)
    state['score'] = 5
    state['image'] = pygame.image.load( 'heart.png' )
    
    state['direction'] = (-1,-1)
    state['score'] = 4
    
    print( "Score is", status['score'] )
    print(state)

Back to Your Game
-----------------

:doc:`heartclickplusplus`
