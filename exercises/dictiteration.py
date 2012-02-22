#! /usr/bin/env python
# dictiteration.py

dictionary = {'this':'that'}
dictionary[ ' this ' ] = 'thar'
dictionary[ 45 ] = 8
dictionary[ 45.0 ] = 9

print 'items',dictionary.items() # [('this','that')]
print 'values',dictionary.values() # ['that']
print 'keys', dictionary.keys() # ['this']

print
for key in dictionary:
    print '{!r} : {}'.format( key, dictionary[key] )

# Super Bonus Ask During Coffee Question: why is the key 45 and not 45.0?
