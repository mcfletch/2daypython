#! /usr/bin/env python
# functionsimple.py

def double( value ):
    """returns the value multiplied by two"""
    return value * 2

def larger( first, second):
    """Return the larger of first and second"""
    if first >= second:
        return first 
    else:
        return second 

print 'double of the larger of 3 and 4:',double( larger( 3,4 ))
# print value # doesn't work
