#! /usr/bin/env python

measurements = range( 30 )

print 'Odd Triple Squares'
total = 0
for item in measurements:
    if item % 2 and not item % 3:
        print item, item ** 2
        total += item **2
print 'Sum of Odd Triple Squares:', total
