#!/usr/bin/env python3
import sys


def check_for_word_len(lenght, d):
    total = 0
    for w in d:
        if len(w) == lenght:
            total += d[w]
    print("Total amount of len {} words: {}".format(lenght, total))

def main(argv):
    current_word = None
    current_count = 0
    word = None

    wc = {}
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

    check_for_word_len(3, wc)
    check_for_word_len(5, wc)

if __name__ == "__main__":
  main(sys.argv)