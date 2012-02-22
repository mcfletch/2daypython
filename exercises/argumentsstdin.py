#! /usr/bin/env python
# argumentsstdin.py
import sys
header = sys.stdin.readline()
for line in sys.stdin:
    print float(line.split(',')[2])
