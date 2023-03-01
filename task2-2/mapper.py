#!/usr/bin/env python3
import sys
import re
# from validators import domain

pattern = re.compile(
    r'^(?:[a-zA-Z0-9]'  # First character of the domain
    r'(?:[a-zA-Z0-9-_]{0,61}[A-Za-z0-9])?\.)'  # Sub domain + hostname
    r'+[A-Za-z0-9][A-Za-z0-9-_]{0,61}'  # First 61 characters of the gTLD
    r'[A-Za-z]$'  # Last character of the gTLD
)


def to_unicode(obj, charset='utf-8', errors='strict'):
    if obj is None:
        return None
    if not isinstance(obj, bytes):
        return str(obj)
    return obj.decode(charset, errors)


def domain(value):
    try:
        return pattern.match(to_unicode(value).encode('idna').decode('ascii'))
    except (UnicodeError, AttributeError):
        return False

def main(argv):
    for line in sys.stdin: 
        # remove leading and trailing whitespace 
        line = line.strip() 
        # split the line into words 
        words = line.split()
        d = words[0]
        if domain(d): # Strip non-valid domains
            print('%s\t%s' % (d, 1))

if __name__ == "__main__":
  main(sys.argv)