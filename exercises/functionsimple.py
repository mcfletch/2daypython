#! /usr/bin/env python

def double( value ):
    """returns the value multiplied by two"""
    return value * 2

def larger( first, second):
    """Return the larger of first and second"""
    if first >= second:
        return first 
    else:
        return second 

print double( larger( 2,3 ))
