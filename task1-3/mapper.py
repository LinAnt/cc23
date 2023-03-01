#!/usr/bin/env python3
import sys

wc = {}
for line in sys.stdin: 
    # remove leading and trailing whitespace 
    line = line.strip() 
    # split the line into words 
    words = line.split() 
    # increase counters 
    for word in words:
        if not word.isalpha(): # Drop all non alpha words
            continue
        # count words in current chunk
        if word in wc:
            count = wc[word]
            wc[word] = count + 1
        else:
            wc[word] = 1

# print values in same format as before
for w in wc:
    print('%s\t%s' % (w, wc[w]))

if __name__ == "__main__":
  main(sys.argv)