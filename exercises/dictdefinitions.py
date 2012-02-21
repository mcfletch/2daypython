#! /usr/bin/env python

dictionary = {}
dictionary['this'] = 'that'
dictionary['those'] = 23
assert dictionary['those'] == 23
del dictionary['those']
dictionary.get( 'those' ) # returns None 
dictionary.get( 'those', 3 ) # returns 3
dictionary.get( 'this' ) # returns 'that'

print dictionary.items() # [('this','that')]
print dictionary.values() # ['that']
print dictionary.keys() # ['this']

dictionary2 = {
    'thar': 'thusly',
    'them': 'tharly',
}
