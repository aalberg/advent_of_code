import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import re
import time

PART = 1
TEST = 0
PROBLEM = 4
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"

grid = []
e = []
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
DIRS2 = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
WORD = "XMAS"
WORD2 = "MAS"


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def inbounds(x, y):
  return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)
      e.append([0] * len(line))

  for l in grid:
    print(l)

  count = 0
  for xs in range(len(grid)):
    for ys in range(len(grid[0])):
      for d in DIRS:
        ok = True
        for i, c in enumerate(WORD):
          xc = xs + d[0]*i
          yc = ys + d[1]*i
          if not inbounds(xc, yc) or grid[xc][yc] != c:
            ok = False
            break
        if ok:
          count += 1
  #         for i in range(len(WORD)):
  #           e[xs + d[0]*i][ys + d[1]*i] = 1
  # for l in e:
  #     print(l)
  print(count)

  count2 = 0
  for xs in range(1, len(grid) - 1):
    for ys in range(1, len(grid[0]) - 1):
      if grid[xs][ys] != "A":
        continue
      ok_count = 0
      for d in DIRS2:
        ok = True
        for i, c in enumerate(WORD2):
          xc = xs + d[0]*(i - 1)
          yc = ys + d[1]*(i - 1)
          if not inbounds(xc, yc) or grid[xc][yc] != c:
            ok = False
            break
        if ok:
          ok_count += 1
      if ok_count == 2:
        count2 += 1
        e[xs][ys] = 1

  for l in e:
    print(l)

  print(count2)



if __name__ == "__main__":
  main()
