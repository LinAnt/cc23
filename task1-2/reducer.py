#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None
wc = {} 

def sort_and_return_top_100(d):
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for k,v in sorted_dict[:100]:
        print(k, v)

def main(argv):
    for line in sys.stdin:
        # remove leading and trailing whitespaces
        line = line.strip()
        # parse the input we got from mapper.py
        word, count = line.split('\t', 1)
        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue
        if current_word == word:
            current_count += count
        else:
            if current_word:
                wc[str(current_word)] = current_count
            current_count = count
            current_word = word
    if current_word == word:
        wc[str(current_word)] = current_count

    sort_and_return_top_100(wc)


if __name__ == "__main__":
  main(sys.argv)