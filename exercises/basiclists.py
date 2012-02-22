#! /usr/bin/env python
# basiclists.py

# We often want to process "lists" of data
# (We could build the same list with a call to range( 10 ))
integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print 'integers', integers
# We can pull values out of a list
print 'first item', integers[0]
print 'seventh item', integers[6]

# A negative index in *python* starts counting from the *end* of the 
# list, so -1 is the last item, -2 is the second-last, etc
print 'last item', integers[-1]

# We can add values to the end of the list 
integers.append( 11 )
print 'new last item',integers[-1]
print 'integers', integers

# We can insert values at an arbitrary location as well...
integers.insert( 0, -1 )
print 'new first item',integers[0]
print 'integers', integers

# And we can delete values (note the special syntax here)
del integers[0]
print 'new new first item', integers[0]
print 'integers', integers

# And we can find out how long the list is (note: most languages 
# use "integers.length", *python* is not the norm here...
print 'length', len(integers)

# Note: while *normally* we want our lists to contain the same "type"
# of data, lists (in Python) do not enforce that restriction
integers.append( 'apple' )
print 'mixed types', integers
