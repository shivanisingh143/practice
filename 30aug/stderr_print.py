from __future__ import print_function
import sys

def eprn(*arg, **kwargs):
    print(*arg, file=sys.stderr, **kwargs)

eprn("abc", "def", "ghi", sep="--")