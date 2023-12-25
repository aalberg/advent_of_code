import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 10
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d_2.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)

grid = []
visited = {}

def inbounds(xy):
  return xy[0] >= 0 and xy[0] < len(grid[0]) and xy[1] >= 0 and xy[1] < len(grid)

def get_adjacent(xy):
  g = grid[xy[1]][xy[0]]
  if g == "S":
    a = []
    if grid[xy[1]][xy[0] - 1] in "FL-":
      a.append((xy[0] - 1, xy[1]))
    if grid[xy[1]][xy[0] + 1] in "7J-":
      a.append((xy[0] + 1, xy[1]))
    if grid[xy[1] - 1][xy[0]] in "F7|":
      a.append((xy[0], xy[1] - 1))
    if grid[xy[1] + 1][xy[0]] in "JL|":
      a.append((xy[0], xy[1] + 1))
    return a
  elif g == "|":
    return [(xy[0], xy[1] - 1), (xy[0], xy[1] + 1)]
  elif g == "-":
    return [(xy[0] - 1, xy[1]), (xy[0] + 1, xy[1])]
  elif g == "L":
    return [(xy[0] + 1, xy[1]), (xy[0], xy[1] - 1)]
  elif g == "J":
    return [(xy[0] - 1, xy[1]), (xy[0], xy[1] - 1)]
  elif g == "F":
    return [(xy[0] + 1, xy[1]), (xy[0], xy[1] + 1)]
  elif g == "7":
    return [(xy[0] - 1, xy[1]), (xy[0], xy[1] + 1)]
  return []

def get_valid_adjacent(xy):
  return list(filter(lambda a: inbounds(a), get_adjacent(xy)))

def main():
  start = (0, 0)
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)
      s = grid[-1].find("S")
      if s != -1:
        start = (s, len(grid) - 1)

  # Part 1: BFS around the loop
  frontier = deque()
  frontier.append(start)
  visited[start] = 0
  furthest = 0
  while len(frontier) > 0:
    cur = frontier.popleft()
    for a in get_valid_adjacent(cur):
      if a not in visited:
        frontier.append(a)
        visited[a] = visited[cur] + 1
        furthest = visited[a]
  print(furthest)

  # Part 2: Scan the grid and count the pipes we cross, keeping track of if the
  # pipes we've crossed means we're inside or outside the loop.
  # Ugly hack to not deal with the S
  for i in range(len(grid)):
    if TEST == 1:
      grid[i] = grid[i].replace("S", "F")
    else:
      grid[i] = grid[i].replace("S", "|")

  area = 0
  for y in range(len(grid)):
    inside = False
    entry = ""
    for x in range(len(grid[0])):
      xy = (x, y)
      g = grid[y][x]

      if xy in visited:
        # Case 1: Crossing a | always flips our state
        if g == "|":
          inside = not inside
        # Case 2: We're traveling along a pipe. Depending on how we leave we
        # might end up inside or outside. Keep track of how we entered the pipe.
        elif g in "FL":
          entry = g
        # Case 3: We're leaving the pipe we were on. If we took 1 right and
        # 1 left turn to leave the pipe, we changed sides of it.
        elif g in "7J":
          if (entry == "F" and g == "J") or (entry == "L" and g == "7"):
            inside = not inside
          entry = ""
      elif inside:
        area += 1
  print(area)


if __name__=="__main__":
  main()
