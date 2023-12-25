import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 16
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

grid = []

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line

def inbounds(x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def move(cur, d):
  n = tuple([cur[i] + d[i] for i in range(2)])
  if inbounds(n[0], n[1]):
    return [(n, d)]
  return []

def process_tile(cur, d):
  t = grid[cur[1]][cur[0]]
  nd = d
  if t == "|":
    if d[0] != 0:
      new_states = []
      for nd in [(0, -1), (0, 1)]:
        #print("nd", nd)
        new_states.extend(move(cur, nd))
      return new_states
  elif t == "-":
    if d[1] != 0:
      new_states = []
      for nd in [(-1, 0), (1, 0)]:
        new_states.extend(move(cur, nd))
      return new_states
  elif t == "/":
    nd = (-1 * d[1], -1 * d[0])
    #print("nd", nd)
  elif t == "\\":
    nd = (d[1], d[0])
    #print("nd", nd)
  #print("m", move(cur, d))
  return move(cur, nd)

def simulate(start, start_d, print_final=False):
  e = []
  for i in range(len(grid)):
    e.append([0] * len(grid[0]))
  visited = {}
  frontier = deque()

  visited[(start, start_d)] = True
  frontier.append((start, start_d))
  #print(frontier)
  while len(frontier) > 0:
    cur, d = frontier.popleft()
    #print("cur", cur, d)
    e[cur[1]][cur[0]] = 1
    #print("  ", process_tile(cur, d))
    for p in process_tile(cur, d):
      n, nd = p[0], p[1]
      if (n, nd) not in visited:
        visited[(n, nd)] = True
        frontier.append((n, nd))

  if print_final:
    for l in grid:
      print(l)
    for l in e:
      print(l)
  return sum([sum(l) for l in e])

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)
  # for l in grid:
  #   print(l)
  # for l in e:
  #   print(l)

  print("part1:", simulate((0, 0), (1, 0)))

  best_score = -1
  best_start = None


  for x in range(len(grid[0])):
    for sd in range(-1, 2, 2):
      start = (x, 0 if sd == 1 else (len(grid) - 1))
      start_d = (0, sd)
      score = simulate(start, start_d)
      #print("x", x, start, start_d, score)
      if score > best_score:
        best_score = score
        best_start = (start, start_d)

  for y in range(len(grid[0])):
    for sd in range(-1, 2, 2):
      start = (0 if sd == 1 else (len(grid) - 1), y)
      start_d = (sd, 0)
      score = simulate(start, start_d)
      #print("y", y, start, start_d, score)
      if score > best_score:
        best_score = score
        best_start = (start, start_d)
  print(best_score, best_start, simulate(best_start[0], best_start[1], True))


if __name__=="__main__":
  main()
