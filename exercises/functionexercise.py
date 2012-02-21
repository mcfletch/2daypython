#! /usr/bin/env python

# we get a list of integers we would like to process...
first = []
last = []
for row in open('sample_data.csv').read().splitlines()[1:]:
    split = row.split(',')
    first.append( int(split[1]))
    last.append( int(split[-2]))

print first 
print last
# define a function that returns the largest integer in the list 
# define another function which returns the sum of the integers in the list 
# display the largest integer in both lists 
# display the sum of both lists 
# display the average of both lists
