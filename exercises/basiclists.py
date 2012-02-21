#! /usr/bin/env python

# We often want to process "lists" of data
measurements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print 'measurements', measurements
# We can pull values out of a list
print 'first item', measurements[0]
print 'seventh item', measurements[6]

# A negative index in *python* starts counting from the *end* of the 
# list, so -1 is the last item, -2 is the second-last, etc
print 'last item', measurements[-1]

# We can add values to the end of the list 
measurements.append( 11 )
print 'new last item',measurements[-1]
print 'measurements', measurements

# We can insert values at an arbitrary location as well...
measurements.insert( 0, -1 )
print 'new first item',measurements[0]
print 'measurements', measurements

# And we can delete values (note the special syntax here)
del measurements[0]
print 'new new first item', measurements[0]
print 'measurements', measurements

# And we can find out how long the list is (note: most languages 
# use "measurements.length", *python* is not the norm here...
print 'length', len(measurements)

# Note: while *normally* we want our lists to contain the same "type"
# of data, lists (in Python) do not enforce that restriction
measurements.append( 'apple' )
print 'mixed types', measurements
