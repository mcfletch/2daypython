#! /usr/bin/env python

# An "integer" (a whole number)
count = 36

# Working with integers can be surprising
print 'count', count
print 'count / 10:', count/10
# Note: that was *truncation*, *not* rounding

# A floating-point number
irrational = 3.141592653589793
# We can convert values to/from floating point and integer...
print 'float(count):', float( count )
print 'float(count)/10:', float( count )/10

# These are strings of text, the quotes in *python*
# can be either type, other languages may constrain the 
# type of quotes used.
label = "irrational"
label2 = 'count'
print label, label2
print label + label2
