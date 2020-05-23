#! /usr/bin/env python
# argumentsstdin.py
from __future__ import absolute_import
from __future__ import print_function
import sys
header = sys.stdin.readline()
for line in sys.stdin:
    print(float(line.split(',')[2]))
