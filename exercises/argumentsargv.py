#! /usr/bin/env python
# argumentsargv.py

import sys

def print_files( files ):
    """A function another module might want to invoke"""
    for file in files:
        print file 

def main():
    """Primary entry point for the script/module"""
    if sys.argv[1:]:
        print_files( sys.argv[1:] )
        return 0
    else:
        sys.stderr.write( "You need to provide file[s]\n" )
        return 1

if __name__ == "__main__":
    sys.exit( main())
