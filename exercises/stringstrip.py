#! /usr/bin/env python
# stringstrip.py

value = '  25.3  '
clean = value.strip()
# value == '25.3'

quoted = '"this"'
clean = quoted.strip('"')
# clean == 'this'
