import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 15
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)

def fakehash(s):
  cur = 0
  for c in s:
    cur += ord(c)
    cur *= 17
    cur = cur % 256
  return cur

def main():
  tokens = []
  with open(in_file, 'r') as f:
    tokens = f.readline().split(",")

  total = 0
  hashmap = defaultdict(list)
  for token in tokens:
    total += fakehash(token)
    if token[-1] == "-":
      h = fakehash(token[:-1])
      for i, p in enumerate(hashmap[h]):
        if p[0] == token[:-1]:
          del hashmap[h][i]
    else:
      label, val = token.split("=")
      val = int(val)
      h = fakehash(label)
      added = False
      for i, p in enumerate(hashmap[h]):
        if p[0] == label:
          hashmap[h][i] = (label, val)
          added = True
      if not added:
        hashmap[h].append((label, val))

  fl = 0
  for b in range(256):
    for i, item in enumerate(hashmap[b]):
      fl += (b + 1) * (i + 1) * item[1]
  print("part 1:", total)
  print("part 2:", fl)

if __name__=="__main__":
  main()
