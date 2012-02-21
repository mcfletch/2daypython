#! /usr/bin/env python

# A number with which we want to work
count = 5.0

print 'count:', count 

# Mathematics works pretty-much as you would expect
print 'count + 3:', count + 3
print 'count * 3:', count * 3
print 'count / 3:', count / 3.0
print 'count ** 2:', count ** 2
print 'count ** .5:', count ** .5
print 'count % 3:', count % 3
print 'count // 3:', count // 3

# We have brackets for overriding order of operations...
print 'count * 3 + 2:', count * 3 + 2
print 'count * (3 + 2):', count * (3 + 2)

# We can modify the value stored in the variable
count = count + 3
print 'new count', count
