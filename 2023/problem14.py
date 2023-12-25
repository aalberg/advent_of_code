import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 14
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

grid = []
x_max = 0
y_max = 0
visited = {}

def place_rocks(x, y, x_dir, y_dir, c):
  for i in range(1, c + 1):
    xr = x - i * x_dir
    yr = y - i * y_dir
    grid[yr][xr] = "O"

def tilt(x_dir, y_dir):
  if x_dir == 0:
    ys = 0 if y_dir == 1 else y_max - 1
    ye = y_max if y_dir == 1 else -1
    for x in range(0, x_max):
      c = 0
      for y in range(ys, ye, y_dir):
        if grid[y][x] == "O":
          grid[y][x] = "."
          c += 1
        elif grid[y][x] == "#":
          place_rocks(x, y, x_dir, y_dir, c)
          c = 0
      if c >= 0:
        place_rocks(x, ye, x_dir, y_dir, c)
  else:
    xs = 0 if x_dir == 1 else x_max - 1
    xe = x_max if x_dir == 1 else -1
    for y in range(0, y_max):
      c = 0
      for x in range(xs, xe, x_dir):
        if grid[y][x] == "O":
          grid[y][x] = "."
          c += 1
        elif grid[y][x] == "#":
          place_rocks(x, y, x_dir, y_dir, c)
          c = 0
      if c >= 0:
        place_rocks(xe, y, x_dir, y_dir, c)

def compute_load():
  load = 0
  for x in range(0, x_max):
    for y in range(0, y_max):
      if grid[y][x] == "O":
        load += y_max - y
  return load

def print_grid():
  for l in grid:
    print("".join(l))
  print("-----------")

def grid_to_str():
  output = ""
  for l in grid:
    output += "".join(l)
  return output

def spin_cycle():
  tilt(0, -1)
  tilt(-1, 0)
  tilt(0, 1)
  tilt(1, 0)

def part1():
  tilt(0, -1)
  print("load", compute_load())

T = 1000000000

def part2():
  prev = grid_to_str()
  cur = ""
  visited[prev] = 0
  i = 0
  while i < T:
    spin_cycle()
    cur = grid_to_str()
    if cur in visited:
      print("loop found", visited[cur], i)
      break
    else:
      visited[cur] = i
    prev = cur
    i += 1
  ls = visited[cur]
  le = i 
  loop_len = le - ls
  loops = int((T - ls) / loop_len)
  after_looping = ls + loops * loop_len + 1
  rem = T - after_looping
  print(ls, le, loop_len, loops, after_looping, rem)
  for i in range(rem):
    spin_cycle()

  print("load", compute_load())

def main():
  global x_max
  global y_max
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      grid.append(list(line))
  x_max = len(grid[0])
  y_max = len(grid)
  part1()
  part2()


if __name__=="__main__":
  main()
