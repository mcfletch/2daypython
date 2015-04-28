#! /usr/bin/env python
import sys
def main():
    content = open( sys.argv[1] ).read()
    for line in content.splitlines():
        if '#' in line:
            line = line.split('#',1)[0]
        line = line.rstrip()
        if line:
            print line 

if __name__ == "__main__":
    main()
