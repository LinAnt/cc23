import sys

wc = {}
for line in sys.stdin: 
    # remove leading and trailing whitespace 
    line = line.strip() 
    # split the line into words 
    words = line.split() 
    # increase counters 
    for word in words: 
        # count words in current chunk
        if word in wc:
            count = wc[word]
            wc[word] = count + 1
        else:
            wc[word] = 1

# print values in same format as before
for w in wc:
    print('%s\t%s' % (w, wc[w]))
