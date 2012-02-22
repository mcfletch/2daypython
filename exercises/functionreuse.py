#! /usr/bin/env python
# functionreuse.py

def pretty_print_add(x, y):
    """
    nicely print the addition of two things
    """
    template = '{} + {} = {}'
    print template.format(x, y, x + y)


pretty_print_add(8, 9)

pretty_print_add(4.5, 5.6)

pretty_print_add((1,2), (3,4))

pretty_print_add([5,6], [7,8])
