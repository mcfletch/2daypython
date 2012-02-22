#! /usr/bin/env python
# fileread.py

with open('../sample_data.csv', 'r') as f:
    lines = f.read()

print lines     # a really long string
print lines.splitlines()    # list of strings
