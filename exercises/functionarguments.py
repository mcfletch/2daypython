#! /usr/bin/env python

def extract_column( rows, column=0 ):
    """Extract a column from a set of rows"""
    result = []
    for row in rows:
        result.append( row[column] )
    return result

def extract_columns( rows, *columns ):
    """Extract an arbitrary number of columns from the given rows"""
    result = []
    for column in columns:
        result.append( extract_column( rows, column ))
    return result
