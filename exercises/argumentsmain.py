#! /usr/bin/env python
# argumentsmain.py

from __future__ import absolute_import
import sys

def main():
    """Primary entry point for the script/module"""
    return 1

# A python-only idiom meaning "only execute this if we are the top-level script"
# i.e. do *not* run this if we are being imported as a module
if __name__ == "__main__":
    sys.exit( main())
