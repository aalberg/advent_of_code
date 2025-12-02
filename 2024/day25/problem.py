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
PROBLEM = 25
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

keys = set()
locks = set()

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line

def find_heights(grid):
  heights = []
  for x in range(len(grid[0])):
    #print("x ", x)
    for i, line in enumerate(grid) if grid[0][0] == "#" else enumerate(reversed(grid)):
      #print("line ", line)
      if line[x] != "#":
        #print("i", i)
        heights.append(i)
        break

  return tuple(heights), grid[0][0] == "#"

def overlaps(k, l):
  for i, ke in enumerate(k):
    if ke + l[i] > 7:
      return True
  return False

def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    grid = []
    for line in f:
      line = line.rstrip()
      if not line:
        heights, is_key = find_heights(grid)
        if is_key:
          keys.add(heights)
        else:
          locks.add(heights)
        for l in grid:
          print(l)
        print(heights, is_key)
        grid = []
        continue
      grid.append(line)
  total = 0
  for k in keys:
    for l in locks:
      if not overlaps(k, l):
        total += 1
  print("total ", total)


if __name__ == "__main__":
  main()
