#! /usr/bin/env python
# functionexercise.py

# we're going to use those column-extractors we just defined, we'll discuss 
# how this works later...
from __future__ import absolute_import
from __future__ import print_function
from .functionarguments import *
# we load up some sample data (we'll cover how this works later)
rows = split_rows( open('../sample_data.csv').read().splitlines()[1:] )
first,second = extract_columns( rows, 1, -2 )
first,second = as_type( first, int ), as_type( second, int )

print(first) 
print(second)
# define a function that returns the largest integer in the list 
# define another function which returns the sum of the integers in the list 
# display the largest integer in both lists 
# display the sum of both lists 
# display the average (mean) of both lists
