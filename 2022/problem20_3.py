import string
from collections import defaultdict
import functools
import sys

with open(r"input20.txt") as f:
    s = f.read().strip()
#print("\n".join(x[:60] for x in s.split("\n")[:6]))

class Node:
    def __init__(self, value, prv=None, nxt=None):
        self.value = value
        self.prv = prv
        self.nxt = nxt

part = 2
dkey = 1 if part == 1 else 811589153

r = []
for l in s.split("\n"):
    n = dkey * int(l)
    r.append(Node(n))


for a,b in zip(r,r[1:]):
    a.nxt = b
    b.prv = a

r[-1].nxt = r[0]
r[0].prv = r[-1]

for itr in range(1 if part == 1 else 10):
    for x in r:
        x.prv.nxt = x.nxt
        x.nxt.prv = x.prv
        a,b = x.prv, x.nxt
        move = x.value % (len(r) - 1)
        for _ in range(move):
            a=a.nxt
            b=b.nxt
        # original code for part 1 had a separate move < 0 case
        # became unnecessary with mod (len(r) - 1)
        a.nxt = x
        x.prv = a
        b.prv = x
        x.nxt = b

for x in r:
    if x.value == 0:
        r = 0
        y = x
        for _ in range(3):
            for _ in range(1000):
                y = y.nxt
            print(y.value)
            r += y.value
        print(r)