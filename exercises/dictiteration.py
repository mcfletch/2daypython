#! /usr/bin/env python
# dictiteration.py

dictionary = {'this':'that','those':'thar',23:18,None:5}

print 'items',dictionary.items()
print 'values',dictionary.values()
print 'keys', dictionary.keys()

for key in dictionary:
    print '{!r} : {}'.format( key, dictionary[key] )
