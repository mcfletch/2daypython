#! /usr/bin/env python
# iterforxiny.py

from __future__ import print_function
measurements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Squares')
total = 0
for item in measurements:
    print(item, item ** 2)
    total += item **2
print('Sum of Squares:', total)
