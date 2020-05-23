#! /usr/bin/env python
# reusecsv.py
from __future__ import absolute_import
import csv
lines = list(csv.reader(open('../sample_data.csv')))[1:]
