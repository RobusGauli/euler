import os
import sys
from collections import defaultdict
from collections import Counter
from collections import namedtuple
from collections import ChainMap

from itertools import islice, groupby, filterfalse, takewhile, repeat, cycle, zip_longest

def even_fib_sum(n):
    a, b = 0, 1
    s = 0
    while a <= n:
        if a % 2 == 0:
            print(a)
            s += a
        a, b = b, a + b
    
    return s
