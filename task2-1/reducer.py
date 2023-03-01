#!/usr/bin/env python3
import sys

req = 0
tot_bytes = 0
 

for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip()
    # parse the input we got from mapper.py
    domain, bytes = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        bytes = int(bytes)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    req += 1
    tot_bytes += bytes



print("Total amount of reqs: {}".format(req))
print("Total transferred GBs: {}".format((tot_bytes/(1024*1024*1024)))) # Ugly conversion to GB
