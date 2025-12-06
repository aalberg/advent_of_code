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
PROBLEM = 4
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]

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

def count_adj(x, y):
  count = 0
  for dir in DIRS:
    nx, ny = x + dir[0], y + dir[1]
    if inbounds(nx, ny) and grid[ny][nx] == '@':
      count += 1
  return count

def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      grid.append(list(line))
      e.append([0] * len(line))
  #for l in grid:
  #  print(l)
  #for l in e:
  #  print(l)

  count = 0
  changed = True
  while changed:
    changed = False
    for y in range(len(grid)):
      for x in range(len(grid[0])):
        if grid[y][x] == '@' and count_adj(x, y) < 4:
          #print(x, y)
          grid[y][x] = '.'
          changed = True
          count += 1
  print(count)


if __name__ == "__main__":
  main()
