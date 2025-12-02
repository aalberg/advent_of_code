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
PROBLEM = 8
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"

grid = []
e = []
antennas = defaultdict(list)
antinodes = set()
antinodes2 = set()

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def inbounds(x, y):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def antinodes_of(p1, p2, part):
  diff = [p1[i] - p2[i] for i in range(2)]
  an = []

  if part == 1:
    an.append(tuple([p1[i] + diff[i] for i in range(2)]))
    an.append(tuple([p2[i] - diff[i] for i in range(2)]))
  if part == 2:
    a = p1
    while inbounds(a[0], a[1]):
      an.append(tuple(a))
      a = [a[i] + diff[i] for i in range(2)]

    a = p2
    while inbounds(a[0], a[1]):
      an.append(tuple(a))
      a = [a[i] - diff[i] for i in range(2)]
  #print(p1, p2, a1, a2, diff)
  return an

def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)
      e.append([0] * len(line))
  for l in grid:
    print(l)


  for x in range(len(grid[0])):
    for y in range(len(grid)):
      if grid[y][x] != ".":
        #print(grid[y][x])
        c = grid[y][x]
        for a in antennas[c]:
          for n in antinodes_of((x, y), a, 1):
            if inbounds(n[0], n[1]):
              antinodes.add(n)
          for n in antinodes_of((x, y), a, 2):
            if inbounds(n[0], n[1]):
              antinodes2.add(n)
        antennas[c].append((x, y))
  # for p in antinodes:
  #   e[p[1]][p[0]] = 1
  # for l in e:
  #   print(l)

  print(len(antinodes))
  print(len(antinodes2))



if __name__ == "__main__":
  main()
