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
PROBLEM = 14
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid = []
e = []
robots = []


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


STEPS = 100
DIMS = [11, 7] if TEST == 1 else [101, 103]

def inbounds(x, y):
  return 0 <= x < len(DIMS[0]) and 0 <= y < len(DIMS[1])

def move_robot(p, v, steps):
  cycle_len = math.lcm(math.lcm(v[0], DIMS[0]), math.lcm(v[1], DIMS[1]))

  req = steps % cycle_len
  #print(cycle_len)

  return [(p[i] + req * v[i]) % DIMS[i] for i in range(2)]

def move_step(p, v):
  return [(p[i] + v[i]) % DIMS[i] for i in range(2)]

def move_all_robots():
  for i, r in enumerate(robots):
    robots[i][0] = move_step(r[0], r[1])

def print_grid(iter):
  for g in grid:
    for i in range(len(g)):
      g[i] = 0
  for r in robots:
    grid[r[0][1]][r[0][0]] = 1
  with open(f"{iter}.txt", "w", encoding="utf-8") as out_file:
    for l in grid:
      s = ""
      for c in l:
        s += str(c)
      out_file.write(s + "\n")

def maybe_tree(iter):
  robot_pos = set()
  for r in robots:
    robot_pos.add(tuple(r[0]))
  adj_robots = 0
  for r in robots:
    if (r[0][0] + 1, r[0][1]) in robot_pos or (r[0][0] - 1, r[0][1]) in robot_pos or (r[0][0], r[0][1] - 1) in robot_pos or (r[0][0], r[0][1] + 1) in robot_pos:
      adj_robots += 1

  is_tree = adj_robots >= 300
  if is_tree:
    print(f"{iter} hori {adj_robots}")
  return is_tree

def main():
  qs = [0, 0, 0, 0]
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      line = [i[2:] for i in line.split(" ")]
      p = [int(i) for i in line[0].split(",")]
      v = [int(i) for i in line[1].split(",")]

      f = move_robot(p, v, STEPS)
      q = -1
      if f[0] < DIMS[0] // 2 and f[1] < DIMS[1] // 2:
        q = 0
      elif f[0] > DIMS[0] // 2 and f[1] < DIMS[1] // 2:
        q = 1
      elif f[0] < DIMS[0] // 2 and f[1] > DIMS[1] // 2:
        q = 2
      elif f[0] > DIMS[0] // 2 and f[1] > DIMS[1] // 2:
        q = 3
      #print(p, v, f, q)
      if q >= 0:
        qs[q] += 1
      #break

      robots.append([p, v])
  total = 1
  for q in qs:
    total *= q
  print(total, qs)

  # part 2
  print(robots)
  for _ in range(DIMS[1]):
    grid.append(list([0] * DIMS[0]))
  for i in range(10000):
    #print(i)
    move_all_robots()
    if maybe_tree(i):
      print_grid(i)




if __name__ == "__main__":
  main()
