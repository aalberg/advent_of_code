import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import re
import time

PART = 2
TEST = 0
PROBLEM = 15
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test2.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid = []
e = []


def nextline(f) -> str:
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def inbounds(x, y):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def push_in_dir(p, d):
  n = [p[i] + DIRS[d][i] for i in range(2)]

  b = list(n)
  while grid[b[1]][b[0]] == "O":
    b = [b[i] + DIRS[d][i] for i in range(2)]

  if grid[b[1]][b[0]] == "#":
    return p

  grid[b[1]][b[0]] = "O"
  grid[n[1]][n[0]] = "@"
  grid[p[1]][p[0]] = "."
  return n

def get_box_part(b):
  if grid[b[1]][b[0]] == "[":
    return (b[0]+1, b[1])
  if grid[b[1]][b[0]] == "]":
    return (b[0]-1, b[1])
  return None

def push_in_dir2(p, d):
  n = [p[i] + DIRS[d][i] for i in range(2)]

  if grid[n[1]][n[0]] ==  "#":
    return p

  if grid[n[1]][n[0]] in "[]":
    if d in (0, 2):
      to_move = []
      f = set()
      f.add(tuple(n))
      f.add(get_box_part(n))
      for b in f:
        to_move.append(b)

      while len(f) > 0:
        new_f = set()
        for b in f:
          b2 = [b[i] + DIRS[d][i] for i in range(2)]
          if grid[b2[1]][b2[0]] == "#":
            return p
          if grid[b2[1]][b2[0]] in "[]":
            new_f.add(tuple(b2))
            new_f.add(get_box_part(b2))
        f = new_f
        for b in f:
          to_move.append(b)
      # print("tomove: ", to_move)
      for b in reversed(to_move):
        grid[b[1] + DIRS[d][1]][b[0]] = grid[b[1]][b[0]]
        grid[b[1]][b[0]] = "."

    else:
      b = list(n)
      while grid[b[1]][b[0]] in "[]":
        b[0] += DIRS[d][0]

      if grid[b[1]][b[0]] == "#":
        return p

      while b[0] != n[0]:
        x1, x2 = b[0], b[0] - DIRS[d][0]
        grid[b[1]][min(x1, x2)] = "["
        grid[b[1]][max(x1, x2)] = "]"
        b[0] -= 2*DIRS[d][0]

  grid[n[1]][n[0]] = "@"
  grid[p[1]][p[0]] = "."
  return n

def char_to_dir(c):
  if c == "<":
    return 3
  if c == "^":
    return 0
  if c == ">":
    return 1
  if c == "v":
    return 2
  return None

def transform_line(line):
  if PART == 1:
    return list(line)
  new_line = ["."] * (len(line) * 2)
  for i, c in enumerate(line):
    if c == "#":
      new_line[2*i] = "#"
      new_line[2*i+1] = "#"
    elif c == "O":
      new_line[2*i] = "["
      new_line[2*i+1] = "]"
    elif c == ".":
      new_line[2*i] = "."
      new_line[2*i+1] = "."
    elif c == "@":
      new_line[2*i] = "@"
      new_line[2*i+1] = "."
  return new_line

def main():
  start = 0
  #boxes = set()
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    line = "."
    while len(line) > 0:
      line = nextline(f)
      for i, c in enumerate(line):
        if c == "@":
          start = (i, len(grid))
          if PART == 2:
            start = (2 * i, len(grid))

      if len(line) > 0:
        grid.append(transform_line(line))

    # for l in grid:
    #   print(l)

    line = "."
    pos = start
    while len(line) > 0:
      line = nextline(f)
      #print(line)
      for c in line:
        # print(c)
        if PART == 1:
          pos = push_in_dir(pos, char_to_dir(c))
        else:
          pos = push_in_dir2(pos, char_to_dir(c))
        # for l in grid:
        #   print(l)

  total = 0
  for y, g in enumerate(grid):
    for x, c in enumerate(g):
      if c in "O[":
        total += 100 * y + x
  print(total)



if __name__ == "__main__":
  main()
