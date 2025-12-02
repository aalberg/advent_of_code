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
PROBLEM = 6
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


def move(cur, d):
  s = (cur[0] + DIRS[d][0], cur[1] + DIRS[d][1])
  if not inbounds(s[0], s[1]):
    return None, None
  if grid[s[1]][s[0]] == "#":
    d = (d + 1) % len(DIRS)
    return cur, d
  return s, d

def do_walk(start):
  visited = set()
  cur = start
  cur_d = 0
  e[start[1]][start[0]] = 1
  visited.add((cur, cur_d))
  while True:
    n, n_d = move(cur, cur_d)
    #print(n, n_d)
    if n is None:
      return visited, False
    e[n[1]][n[0]] = 1
    cur, cur_d = n, n_d
    if (cur, cur_d) in visited:
      return visited, True
    visited.add((cur, cur_d))
  return None, None

def main():
  start = None
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      grid.append(list(line))
      e.append([0] * len(line))
      p = line.find("^")
      if p >= 0:
        start = (p, len(grid) - 1)
  for l in grid:
    print(l)
  print(start)

  initial_visited, _ = do_walk(start)

  # Part 1
  total = 0
  for row in e:
    for visited in row:
      if visited:
        total += 1

  for l in e:
    print(l)
  print(total)

  # Part 2
  total2 = 0
  possible_spots = set()
  for v in initial_visited:
    #print(v)
    possible_spots.add(v[0])
  for p in possible_spots:
    if p == start:
      continue
    #print(p)
    grid[p[1]][p[0]] = "#"
    _, loop = do_walk(start)
    grid[p[1]][p[0]] = "."
    if loop:
      print("loop: ", p)
      total2 += 1
  print(total2)


if __name__ == "__main__":
  main()
