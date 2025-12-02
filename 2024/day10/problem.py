import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import re
import time

PART = 2
TEST = 0
PROBLEM = 10
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
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

def adj(x, y):
  a = []
  for d in DIRS:
    n = (x + d[0], y + d[1])
    if inbounds(n[0], n[1]):
      a.append(n)
  return a

def zero_e():
  for x in range(len(e[0])):
    for y in range(len(e)):
      e[x][y] = 0

def main():
  starts = []
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = list(line.rstrip())
      line = [int(i) for i in line]
      grid.append(line)
      for i, c in enumerate(line):
        if c == 0:
          starts.append((i, len(grid) - 1))
      e.append([0] * len(line))

  for l in grid:
    print(l)
  for l in e:
    print(l)
  print(starts)
  total = 0
  for start in starts:
    score = 0
    f = deque()
    f.append(start)
    #print(start)
    while len(f) > 0:
      c = f.popleft()
      if grid[c[1]][c[0]] == 9:
        #print(f"  {start} {c}")
        score += 1
        continue
      for a in adj(c[0], c[1]):
        #print(f"    {start} {a} {grid[a[1]][a[0]]} {grid[c[1]][c[0]]}")
        if grid[a[1]][a[0]] != grid[c[1]][c[0]] + 1:
          continue
        if e[a[1]][a[0]] == 0:
          f.append(a)
          if PART == 1:
            e[a[1]][a[0]] = 1
    #print(start, score)
    total += score
    zero_e()
  print(f"total {total}")




if __name__ == "__main__":
  main()
