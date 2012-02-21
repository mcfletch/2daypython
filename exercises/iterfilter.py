#! /usr/bin/env python

measurements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print 'Odd Squares'
total = 0
for item in measurements:
    if item % 2:
        print item, item ** 2
        total += item **2
print 'Sum of Odd Squares:', total
