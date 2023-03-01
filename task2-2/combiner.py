#!/usr/bin/env python3
import sys

def main(argv):
    domain_dict = {}
    for line in sys.stdin: 
        # remove leading and trailing whitespace 
        line = line.strip() 
        # split the line into words 
        words = line.split() 
        d = words[0]
        amount = int(words[1])
        if d in domain_dict:
            count = domain_dict[d]
            domain_dict[d] = count + amount
        else:
            domain_dict[d] = amount

    for d in domain_dict:
        print('%s\t%s' % (d, domain_dict[d]))

if __name__ == "__main__":
  main(sys.argv)