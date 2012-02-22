#! /usr/bin/env python
# basictypes.py

# An "integer" (a whole number)
count = 36

# Working with integers can be surprising
print 'count', count
print 'count / 10:', count/10
# Note: that was *truncation*, *not* rounding

# A floating-point number
irrational = 3.141592653589793

# These are strings of text, the quotes in *python*
# can be either type, other languages may constrain the 
# type of quotes used.
label = "irrational"
label2 = 'count'
print label, label2
print label + label2

# The None object is a special object that means "nothing"
print 'None',None 

# The True and False objects represent boolean Truth/Falseness
# They happen to be == to 1 and 0 internally
print 'True',True 
print 'False',False 
