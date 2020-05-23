#! /usr/bin/env python
# reusenumpy.py
from __future__ import absolute_import
from __future__ import print_function
from .functionarguments import *
import csv, numpy
rows = list(csv.reader(open('../sample_data.csv')))[1:]

column = extract_column( rows,1 )
column = as_type(column,float)
print('Max of column [1]',numpy.max( column ))
print('Mean of column [1]',numpy.mean( column ))
print('Median of column [1]',numpy.median( column ))
print('Standard deviation of column [1]',numpy.std( column ))

