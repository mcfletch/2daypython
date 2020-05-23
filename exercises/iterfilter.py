#! /usr/bin/env python
# iterfilter.py

from __future__ import print_function
measurements = range( 30 )

print('Odd Triple Squares')
total = 0
rest = 0
for item in measurements:
    if item == 25:
        print('25 is cool, but not an odd triple')
    elif item % 2 and not item % 3:
        print(item, item ** 2)
        total += item **2
print('Sum of Odd Triple Squares:', total)
