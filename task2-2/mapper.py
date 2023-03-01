import sys
from validators import domain 

domain_dict = {}

for line in sys.stdin: 
    # remove leading and trailing whitespace 
    line = line.strip() 
    # split the line into words 
    words = line.split() 
    d = words[0] 
    if domain(d): # Strip non-valid domains
        if d in domain_dict:
            count = domain_dict[d]
            domain_dict[d] = count + 1
        else:
            domain_dict[d] = 1

for d in domain_dict:
    print('%s\t%s' % (d, domain_dict[d]))
