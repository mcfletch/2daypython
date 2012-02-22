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
label = "irrational 'eh"
label2 = 'count "this"'
label3 = '''python has these too'''
label4 = """and these, but they're just another way of writing the same thing"""
print label, label2, label3, label4
print label + label2

# The None object is a special object that means "nothing"
print None 

# The True and False objects represent boolean Truth/Falseness
# They happen to be == to 1 and 0 internally
print True 
print False 
print 'True == 1', True == 1
