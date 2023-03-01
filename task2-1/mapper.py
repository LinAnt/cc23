#!/usr/bin/env python3
import sys

def main(argv):
    for line in sys.stdin: 
        # remove leading and trailing whitespace 
        line = line.strip() 
        # split the line into words 
        words = line.split() 
        print('%s\t%s' % (words[0], words[-1]))

if __name__ == "__main__":
  main(sys.argv)