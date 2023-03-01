#!/usr/bin/env python3
import sys

def main(argv):
    for line in sys.stdin: 
        # remove leading and trailing whitespace 
        line = line.strip() 
        # split the line into words 
        words = line.split() 
        # increase counters 
        for word in words:
            if not word.isalpha(): # Drop all non alpha words
                continue
            print('%s\t%s' % (word, 1))


if __name__ == "__main__":
  main(sys.argv)