#!/usr/bin/env python3
import sys

def main(argv):
    wc = {}
    for line in sys.stdin: 
        # remove leading and trailing whitespace 
        line = line.strip() 
        # split the line into words 
        words = line.split()

        word = words[0]
        amount = int(words[1])

        # increase counters 
        if word in wc:
            count = wc[word]
            wc[word] = count + amount
        else:
            wc[word] = 1

    # print values in same format as before
    for w in wc:
        print('%s\t%s' % (w, wc[w]))


if __name__ == "__main__":
  main(sys.argv)
