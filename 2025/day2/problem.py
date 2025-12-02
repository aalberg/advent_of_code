import bisect
from collections import defaultdict
from collections import deque
import functools
import heapq
import math
import os
import re
import time

PART = 1
TEST = 0
PROBLEM = 2
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid = []
e = []


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def inbounds(x, y):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def main():
  ids = None
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip().split(",")
      #print(line)
      ids = [[int(i) for i in l.split("-")] for l in line]
      print(ids)
      break
  total = 0
  for pair in ids:
    for i in range(pair[0], pair[1]+1):
      #print("testing:", i)
      s = str(i)
      ok = True
      for numparts in range(2, len(s)+1):
        if len(s) % numparts != 0:
          continue
        seglen = len(s)//numparts
        match = s[0:seglen]
        allmatch = True
        for k in range(numparts):
          #print("     ", match, s[k*seglen:(k+1)*seglen])
          if match != s[k*seglen:(k+1)*seglen]:
            allmatch = False
            break
        if allmatch:
          ok = False
          break
      if allmatch:
        #print("allmatch:", i)
        total += i
  print(total)


if __name__ == "__main__":
  main()
