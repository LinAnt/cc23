#!/usr/bin/env python3
import sys

domain_dict = {} 

def sort_and_return_top_5(d):
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 domains and request count")
    for k,v in sorted_dict[:5]:
        print("Domain: {}, {}".format(k, v))

def main(argv):
    for line in sys.stdin:
        # remove leading and trailing whitespaces
        line = line.strip()
        # parse the input we got from mapper.py
        d, requests = line.split('\t', 1)
        # convert count (currently a string) to int
        try:
            requests = int(requests)
        except ValueError:
            # bytes was not a number, so silently
            # ignore/discard this line
            continue

        # small combiner
        if d in domain_dict:
            count = domain_dict[d]
            domain_dict[d] = count + requests
        else:
            domain_dict[d] = requests

    sort_and_return_top_5(domain_dict)


if __name__ == "__main__":
  main(sys.argv)
