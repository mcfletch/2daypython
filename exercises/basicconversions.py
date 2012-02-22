#! /usr/bin/env python
# basicconversions.py

string = '32'
integer = int( string )
floating = float( integer )
print 'floating', floating

string = '32.6'
floating = float( string )
integer = int( floating )
print 'int(floating)', integer
rounded_int = int( round( floating, 0))
print 'rounded_int', rounded_int
