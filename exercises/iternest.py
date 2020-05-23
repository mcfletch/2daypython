#! /usr/bin/env python
# iternest.py

from __future__ import print_function
rows = [
    ['Lightseagreen Mole', 24.0, -0.906, 0.424, -2.13, 0.0, 'green'],
    ['Indigo Stork', 51.0, 0.67, 0.742, 0.9, 9.0, 'yellow'],
]

for i,row in enumerate( rows ):
    print('rows[{}]'.format( i ))
    for measurement in row[1:-1]:
        print('  {}'.format( measurement ))

