#! /usr/bin/env python
# outputbasic.py
import sys

rows = [
    ['Lightseagreen Mole', 24.0, -0.906, 0.424, -2.13, 0.0, 'green'],
    ['Indigo Stork', 51.0, 0.67, 0.742, 0.9, 9.0, 'yellow'],
]

def format_row( row ):
    result = []
    for item in row:
        result.append( str(item))
    return ",".join( result )

def write_rows( rows, writer ):
    for row in rows:
        writer.write( format_row( row ))
        writer.write( '\n' )
    
def write_file( rows, filename='' ):
    if not filename:
        write_rows( rows, sys.stdout )
    else:
        writer = open( filename,'w')
        write_rows( rows, writer )
        writer.close()

if __name__ == "__main__":
    if sys.argv[1:]:
        write_file( rows, sys.argv[1] )
    else:
        write_file( rows )
    
