#! /usr/bin/env python
# functionisolation.py

def double( value ):
    """returns the value multiplied by two"""
    return value * 2

def raised_double( value, exponent=2 ):
    """Produces value doubled then raised to exponent
    
    value -- number to be operated upon 
    exponent -- exponent to which to raise the doubled value 
    """
    return double(value) ** exponent
