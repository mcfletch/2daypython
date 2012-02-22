#! /usr/bin/env python
# dictoperations.py

dictionary = {}
dictionary['this'] = 'that'
dictionary['those'] = 23

print '{} has {} items'.format( dictionary, len(dictionary))

assert dictionary['those'] == 23

del dictionary['those']

print 'after deletion {} has {} items'.format( dictionary, len(dictionary))

print 'has those?', 'those' in dictionary
print 'has this?', 'this' in dictionary

# Bonus material: you can format keys from a dictionary into strings...
#  print 'We have {this}'.format( **dictionary )
