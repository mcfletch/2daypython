#! /usr/bin/env python
# reusecsv.py
import csv
lines = list(csv.reader(open('../sample_data.csv')))[1:]
