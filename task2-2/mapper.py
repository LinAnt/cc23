#!/usr/bin/env python3
import sys
from validators import domain 

domain_dict = {}

def main(argv):
    for line in sys.stdin: 
        # remove leading and trailing whitespace 
        line = line.strip() 
        # split the line into words 
        words = line.split()
        d = words[0]
        if domain(d): # Strip non-valid domains
            print('%s\t%s' % (d, 1))

if __name__ == "__main__":
  main(sys.argv)