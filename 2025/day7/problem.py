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
PROBLEM = 7
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
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)
      e.append([0] * len(line))
  for l in grid:
    print(l)
  active = set()
  active.add(grid[0].find("S"))
  print(active)
  active2 = defaultdict(int)
  active2[grid[0].find("S")] = 1
  total1 = 0
  for y, row in enumerate(grid):
    print(y, row)
    # for splititer in re.finditer('\^', row):
    #   col = splititer.start()
    #   if col in active:
    #     total1 += 1
    #     active.remove(col)
    #     active.add(col - 1)
    #     active.add(col + 1)
    new_a = defaultdict(int)
    for a, c in active2.items():
      split = False
      for splititer in re.finditer('\^', row):
        col = splititer.start()
        if a == col:
          split = True
          new_a[col - 1] += c
          new_a[col + 1] += c
      if not split:
        new_a[a] += c
    active2 = new_a
    #print(active2)

  print(sum(active2.values()))
  #print(active)
  # print("part 1:", total1)



if __name__ == "__main__":
  main()
