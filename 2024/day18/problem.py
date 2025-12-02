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
TEST = 1
PROBLEM = 18
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

SIZE = 7 if TEST == 1 else 71
STEPS = 12 if TEST == 1 else 1024

grid = []
v = []
sand = []

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def inbounds(x, y):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def adj(p):
  a = []
  for d in DIRS:
    n = (p[0] + d[0], p[1] + d[1])
    a.append(n)
  return a

def reset_grid(g):
  for y in g:
    for i in range(len(y)):
      y[i] = 0

def sim_sand(steps):
  reset_grid(grid)
  for i in range(steps):
    p = sand[i]
    grid[p[1]][p[0]] = 1

def printgrid():
  for gy in grid:
    line = ""
    for gx in gy:
      line += str(gx)
    print(line)

def dijkstras():
  reset_grid(v)
  q = []
  heapq.heappush(q, (0, (0, 0)))

  while q:
    c = heapq.heappop(q)
    if v[c[1][1]][c[1][0]] > 0:
      continue
    v[c[1][1]][c[1][0]] = c[0]
    if c[1][0] == SIZE - 1 and c[1][1] == SIZE - 1:
      return c[0]
    for a in adj(c[1]):
      if inbounds(a[0],
                  a[1]) and grid[a[1]][a[0]] != 1 and v[a[1]][a[0]] == 0:
        heapq.heappush(q, (c[0] + 1, a))
  return None

def binary_search():
  lower = 0
  upper = len(sand)
  mid = 0
  while upper > lower + 1:
    mid = (upper + lower) // 2
    sim_sand(mid)
    result = dijkstras()
    print(lower, mid, upper, result)
    if not result:
      upper = mid
    else:
      lower = mid
  printgrid()
  print("sand piece: ", lower, upper, mid)
  print(sand[lower], sand[upper], sand[mid])
  bound = 5
  for i in range(bound):
    test = mid + bound//2 - i
    sim_sand(test)
    result = dijkstras()
    print(test, sand[test], result)


def main():
  for i in range(SIZE):
    grid.append([0] * SIZE)
    v.append([0] * SIZE)

  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = tuple(int(i) for i in line.rstrip().split(","))
      sand.append(line)

  for i in range(STEPS):
    p = sand[i]
    grid[p[1]][p[0]] = 1

  # printgrid()
  # steps = dijkstras()
  # for l in v:
  #   print(l)
  # print("steps: ", steps)

  binary_search()

if __name__ == "__main__":
  main()
