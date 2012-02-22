#! /usr/bin/env python
# fileread.py

f = open('../sample_data.csv', 'r')     # read only

lines = f.read() # see http://docs.python.org/library/stdtypes.html#file.read

f.close()   # always close

print lines     # a really long string
print lines.splitlines()    # list of strings

l3 = lines.splitlines()[3]
print l3

l3split = l3.split(',')
print l3split

value = l3split[2]
print value, type(value)                # value is str, not good for math

value = float(value)    # convert to float
print float(value), type(float(value))
