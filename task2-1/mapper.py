import sys 
for line in sys.stdin: 
    # remove leading and trailing whitespace 
    line = line.strip() 
    # split the line into words 
    words = line.split() 
    print('%s\t%s' % (words[0], words[-1]))