import bisect
from collections import defaultdict
from collections import deque
import heapq
import functools
import math
import os
import re
import time

PART = 1
TEST = 0
PROBLEM = 16
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test2.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid = []
v = []
e = []


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

def print_visited(visited):
  for ey in e:
    for x in range(len(ey)):
      ey[x] = 0
  for pos in visited:
    e[pos[1]][pos[0]] = 1
  for l in e:
    print(l)

def dijkstras(g, v, start, target):
  print("target", target)
  q = []
  heapq.heappush(q, (0, (start[0], start[1], 1, [start])))
  v[start[1]][start[0]][1] = 0

  min_cost = math.inf
  visited = set()
  while q:
    c = heapq.heappop(q)
    pos = c[1]
    if c[0] > v[pos[1]][pos[0]][pos[2]] and v[pos[1]][pos[0]][pos[2]] != 0:
      #print("killing", c)
      continue
    #print(c[0], c[1][0:3])
    #print(c)
    if pos[0] == target[0] and pos[1] == target[1]:
      #print("end", c)
      if c[0] <= min_cost:
        if c[0] < min_cost:
          min_cost = c[0]
          visited = set()
        for p in c[1][3]:
          visited.add(p)
      else:
        continue

    v[pos[1]][pos[0]][pos[2]] = c[0]

    for d, a in enumerate(adj(pos)):
      if inbounds(
          a[0], a[1]) and g[a[1]][a[0]] != "#" and v[a[1]][a[0]][d] == math.inf:
        new_pos = a
        new_cost = c[0] + 1
        if pos[2] != d:
          new_pos = c[1]
          new_cost = c[0] + 1000
        new_path = list(c[1][3])
        new_path.append(tuple(new_pos[0:2]))
        heapq.heappush(q, (new_cost, (new_pos[0], new_pos[1], d, new_path)))


  # for path in paths:
  #   for p in path:
  #     visited.add(p)
  print("visited", visited)
  print_visited(visited)
  return min_cost, len(visited)


def main():
  start = None
  end = None
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      for i, c in enumerate(line):
        if c == "S":
          start = (i, len(grid))
        elif c == "E":
          end = (i, len(grid))
      grid.append(line)
      e.append([0] * len(line))
      v.append([])
      for _ in range(len(line)):
        v[-1].append([math.inf, math.inf, math.inf, math.inf])
        #print(v)
  for l in grid:
    print(l)
  # for l in v:
  #   print(l)
  cost = dijkstras(grid, v, start, end)
  # for l in grid:
  #  print(l)
  # for l in e:
  #   print(*l, sep='\t')
  # print("---------")
  # for l in v:
  #   print(*l, sep='\t')
  print("cost: ", cost)


if __name__ == "__main__":
  main()
