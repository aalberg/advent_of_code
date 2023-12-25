import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 21
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)

grid = []
x_max = 0
y_max = 0

def inbounds(x, y):
  return x >= 0 and x < x_max and y >= 0 and y < y_max

def adj(cur):
  valid = []
  for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    new_cur = (cur[0] + d[0], cur[1] + d[1])
    if inbounds(new_cur[0], new_cur[1]) and grid[new_cur[1]][new_cur[0]] in ".S":
      valid.append(new_cur)
  return valid

def adj2(cur):
  valid = []
  for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    new_cur = (cur[0] + d[0], cur[1] + d[1])
    if grid[new_cur[1] % y_max][new_cur[0] % x_max] in ".S":
      valid.append(new_cur)
  return valid

MAX_DIST = 10000

def floodfill(start, wrap, max_steps=-1):
  frontier = deque()
  frontier.append((start, 0))
  visited = {}
  visited[start] = 0

  while len(frontier) > 0:
    cur, d = frontier.popleft()
    if max_steps >= 0 and d >= max_steps:
      continue
    next_cur = None
    if not wrap:
      next_cur = adj(cur)
    else:
      next_cur = adj2(cur)
    for n in next_cur:
      if n not in visited:
        frontier.append((n, d + 1))
        visited[n] = d + 1
  return visited

def print_visited(visited):
  for x in range(x_max):
    output = ""
    for y in range(y_max):
      if (x, y) in visited:
        output += f" {visited[(x, y)]:3}"
      else:
        output += "   ."
    print(output)

def count_reachable(visited, max_dist):
  if max_dist < 0:
    return 0
  reachable = 0
  for k, d in visited.items():
    if d <= max_dist and d % 2 == max_dist % 2:
      reachable += 1
  return reachable

totals = defaultdict(int)
mids = defaultdict(int)
bigs = defaultdict(int)
smalls = defaultdict(int)
inner = defaultdict(int)

def solve(x, precompute):
  for s in [(65,0), (65, 130), (0, 65), (130, 65)]:
    mids[x] += count_reachable(precompute[s], 130)
  totals[x] += mids[x]

  for s in [(0, 0), (130,0), (0, 130), (130, 130)]:
    bigs[x] += x * count_reachable(precompute[s], 131 + 64)
    smalls[x] += (x + 1) * count_reachable(precompute[s], 64)
  totals[x] += bigs[x]
  totals[x] += smalls[x]

  count = 1 + 2*x + 2*x*x
  xe = math.floor(x/2)
  even = 1 + 4*xe + 4*xe*xe
  odd = count - even
  inner[x] += even * count_reachable(precompute[(65, 65)], 2 * 131)
  inner[x] += odd * count_reachable(precompute[(65, 65)], 2 * 131 - 1)
  totals[x] += inner[x]

  if x % 2 == 1:
    totals[x] += 156*math.floor(x/2) + 117

def main():
  global x_max
  global y_max
  start = (0, 0)
  with open(in_file, 'r') as f:
    for i, line in enumerate(f):
      line = line.rstrip()
      grid.append(line)
      if "S" in line:
        start = (i, line.find("S"))
  y_max = len(grid)
  x_max = len(grid[0])

  # Part 1
  base = floodfill(start, False, 64)
  print("part 1: ", count_reachable(base, 64))

  MAX_X = 4
  brute = defaultdict(int)
  for x in range(-1, MAX_X):
    steps = 131 * (x + 1) + 65
    base = floodfill(start, True, steps)
    brute[x] = count_reachable(base, steps)
    print("brute", x, brute[x])

  a, b, c = 14669, 14738, 3701
  for x in range(MAX_X):
    print("poly", x, a*x*x + b*x + c)

  precompute = {}
  for s in [(65, 65), (65,0), (65, 130), (0, 65), (130, 65), (0, 0), (130,0), (0, 130), (130, 130)]:
    precompute[s] = floodfill(s, False, 1000)

  print("inner e", count_reachable(precompute[(65, 65)], 1000))
  print("inner o", count_reachable(precompute[(65, 65)], 999))

  for x in range(0, MAX_X):
    solve(x, precompute)
  solve(202300-1, precompute)

  for x in range(0, MAX_X):
    print("totals", x, brute[x], totals[x], mids[x], bigs[x], smalls[x], inner[x], 131 * (x+1) + 65)

  print(totals[202300-1])


if __name__=="__main__":
  main()
