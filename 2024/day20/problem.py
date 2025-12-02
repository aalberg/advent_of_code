import bisect
from collections import defaultdict
from collections import deque
import functools
import heapq
import math
import os
import re
import time

PART = 2
TEST = 0
PROBLEM = 20
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

CHEAT_SIZE = 2 if PART == 1 else 20
grid = []
ds = []
de = []

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

def dijkstras(g, v, start, target):
  print(target)
  q = []
  heapq.heappush(q, (0, start))
  v[start[1]][start[0]] = 0

  cost = math.inf
  while q:
    c = heapq.heappop(q)
    if v[c[1][1]][c[1][0]] != math.inf and v[c[1][1]][c[1][0]] != 0:
      continue
    if c[1][0] == target[0] and c[1][1] == target[1]:
      cost = c[0]
    v[c[1][1]][c[1][0]] = c[0]

    for a in adj(c[1]):
      if inbounds(a[0],
                  a[1]) and g[a[1]][a[0]] != "#" and v[a[1]][a[0]] == math.inf:
        heapq.heappush(q, (c[0] + 1, a))
  return cost

def shortcut_value(g, cost, ds, de, start, end, xd, yd):
  if g[start[1]][start[0]] == "#" or g[end[1]][end[0]] == "#":
    return None
  new_cost = ds[start[1]][start[0]] + abs(xd) + abs(yd) + de[end[1]][end[0]]
  if new_cost >= cost:
    return None
  #print(start, end, cost, ds[start[1]][start[0]], de[end[1]][end[0]])
  return cost - new_cost

def find_shortcuts(g, cost, ds, de):
  cut_values = defaultdict(int)
  for ys in range(1, len(grid) - 1):
    for xs in range(1, len(grid[0]) - 1):
      for yd in range(-CHEAT_SIZE, CHEAT_SIZE+1):
        for xd in range(-CHEAT_SIZE, CHEAT_SIZE+1):
          xe = xs + xd
          ye = ys + yd
          if abs(yd) + abs(xd) > CHEAT_SIZE or not inbounds(xe, ye):
            continue
          value = shortcut_value(g, cost, ds, de, (xs, ys), (xe, ye), xd, yd)
          if value:
            #print(f"({xs}, {ys}) ({xe}, {ye}) {value}")
            cut_values[value] += 1
  total = 0
  for k, v in sorted(cut_values.items()):
    if k >= 100:
      total += v
    print(k, v)
  print(f"cost: {cost}")
  print(f"total: {total}")


def main():
  start = None
  end = None
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      for i, c in enumerate(line):
        if c == "S":
          start = (i, len(grid))
        if c == "E":
          end = (i, len(grid))
      grid.append(line)
      ds.append([math.inf] * len(line))
      de.append([math.inf] * len(line))
  cost = dijkstras(grid, ds, start, end)
  dijkstras(grid, de, end, start)
  # for l in grid:
  #   print(l)
  # print("----")
  # for l in ds:
  #   print(*l, sep='\t')
  # print("----")
  # for l in de:
  #   print(*l, sep='\t')
  find_shortcuts(grid, cost, ds, de)


if __name__ == "__main__":
  main()
