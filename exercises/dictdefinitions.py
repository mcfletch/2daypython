#! /usr/bin/env python
# dictdefinitions.py

dictionary = {}
dictionary['this'] = 'that'
dictionary['those'] = 23
assert dictionary['those'] == 23
del dictionary['those']

print dictionary.items() # [('this','that')]
print dictionary.values() # ['that']
print dictionary.keys() # ['this']

dictionary2 = {
    'thar': 'thusly',
    'them': 'tharly',
}

for key in dictionary2:
    print key, dictionary2[key]
