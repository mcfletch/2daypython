#! /usr/bin/env python
# stringsplit.py

row = 'Silver Deer,69,-0.115,0.993,-0.12,25,violet'
# split the row by the delimiter
columns = row.split(',')
# columns == ['Silver Deer', '69', '-0.115', '0.993', '-0.12', '25', 'violet']
print '\n'.join( columns )
